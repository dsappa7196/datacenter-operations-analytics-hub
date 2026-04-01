"""
Data Center Operations Analytics — Data Pipeline
Author: Padmasree (Padma) Sappa
Description: Loads, validates, and profiles all source tables for the
             analytics hub. Outputs a summary ready for SQL ingestion.
"""

import pandas as pd
import os

# ── Configuration ──────────────────────────────────────────────────────────────

DATA_DIR = "."

TABLES = {
    "operations_daily":              {"grain": ["operations_date", "site_code"],     "fact": True},
    "maintenance_work_orders":       {"grain": ["work_order_id"],                    "fact": True},
    "finance_monthly":               {"grain": ["year_month", "site_code", "cost_center", "spend_category"], "fact": True},
    "customer_experience_monthly":   {"grain": ["year_month", "site_code"],          "fact": True},
    "installed_customer_base_monthly":{"grain": ["year_month", "site_code"],         "fact": True},
    "assets":                        {"grain": ["asset_id"],                         "fact": False},
    "site_dim":                      {"grain": ["site_code"],                        "fact": False},
    "date_dim":                      {"grain": ["calendar_date"],                    "fact": False},
}

# ── Load ───────────────────────────────────────────────────────────────────────

def load_tables(data_dir: str) -> dict[str, pd.DataFrame]:
    """Load all CSV source files into a dictionary of DataFrames."""
    frames = {}
    for table in TABLES:
        path = os.path.join(data_dir, f"{table}.csv")
        if os.path.exists(path):
            frames[table] = pd.read_csv(path)
            print(f"  loaded  {table:<40} {len(frames[table]):>6,} rows")
        else:
            print(f"  missing {table}")
    return frames

# ── Validate ───────────────────────────────────────────────────────────────────

def validate(frames: dict[str, pd.DataFrame]) -> list[str]:
    """
    Run grain and null checks across all tables.
    Returns a list of issue strings — empty list means clean.
    """
    issues = []

    for name, df in frames.items():
        grain_cols = TABLES[name]["grain"]

        # grain uniqueness
        if df.duplicated(subset=grain_cols).any():
            dupes = df.duplicated(subset=grain_cols).sum()
            issues.append(f"{name}: {dupes} duplicate grain rows on {grain_cols}")

        # null check on grain columns
        for col in grain_cols:
            if col in df.columns and df[col].isnull().any():
                issues.append(f"{name}.{col}: contains nulls in grain column")

    return issues

# ── Profile ────────────────────────────────────────────────────────────────────

def profile(frames: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Build a summary table: table name, type, row count, column count,
    date range (where available), and null rate.
    """
    rows = []
    for name, df in frames.items():
        meta = TABLES[name]
        date_col = next((c for c in ["operations_date", "work_order_date",
                                     "year_month", "calendar_date"] if c in df.columns), None)
        date_range = (
            f"{df[date_col].min()} → {df[date_col].max()}" if date_col else "—"
        )
        null_rate = round(df.isnull().mean().mean() * 100, 2)

        rows.append({
            "table":      name,
            "type":       "fact" if meta["fact"] else "dimension",
            "rows":       len(df),
            "columns":    len(df.columns),
            "date_range": date_range,
            "null_%":     null_rate,
        })

    return pd.DataFrame(rows).sort_values("type", ascending=False)

# ── Star Schema Relationships ──────────────────────────────────────────────────

RELATIONSHIPS = [
    ("operations_daily",              "site_code",   "site_dim",   "site_code"),
    ("maintenance_work_orders",       "site_code",   "site_dim",   "site_code"),
    ("finance_monthly",               "site_code",   "site_dim",   "site_code"),
    ("customer_experience_monthly",   "site_code",   "site_dim",   "site_code"),
    ("installed_customer_base_monthly","site_code",  "site_dim",   "site_code"),
    ("maintenance_work_orders",       "asset_id",    "assets",     "asset_id"),
    ("operations_daily",              "operations_date", "date_dim", "calendar_date"),
]

def validate_relationships(frames: dict[str, pd.DataFrame]) -> list[str]:
    """Check referential integrity across all defined relationships."""
    issues = []
    for fact, fk, dim, pk in RELATIONSHIPS:
        if fact not in frames or dim not in frames:
            continue
        fact_keys = set(frames[fact][fk].dropna().unique())
        dim_keys  = set(frames[dim][pk].dropna().unique())
        orphans   = fact_keys - dim_keys
        if orphans:
            issues.append(f"{fact}.{fk} → {dim}.{pk}: {len(orphans)} unmatched keys")
    return issues

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("\n── Loading tables ─────────────────────────────────────────")
    frames = load_tables(DATA_DIR)

    print("\n── Validating grain ───────────────────────────────────────")
    grain_issues = validate(frames)
    if grain_issues:
        for i in grain_issues:
            print(f"  WARN  {i}")
    else:
        print("  all tables pass grain uniqueness checks")

    print("\n── Validating relationships ───────────────────────────────")
    ref_issues = validate_relationships(frames)
    if ref_issues:
        for i in ref_issues:
            print(f"  WARN  {i}")
    else:
        print("  all foreign key relationships are intact")

    print("\n── Table profile ──────────────────────────────────────────")
    summary = profile(frames)
    print(summary.to_string(index=False))

    total_rows = summary["rows"].sum()
    print(f"\n  total records across all tables: {total_rows:,}")
    print(f"  tables loaded: {len(frames)} of {len(TABLES)}")
    print("\n  pipeline complete — ready for Power BI ingestion\n")


if __name__ == "__main__":
    main()
