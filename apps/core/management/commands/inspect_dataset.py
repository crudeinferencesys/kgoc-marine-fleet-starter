"""Management command to quickly profile CSV/Excel datasets at hackathon kickoff."""

from pathlib import Path

import pandas as pd
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Inspect a CSV or Excel dataset (schema, nulls, cardinalities, numeric summary, head)."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to a .csv, .xlsx, or .xls file.")

    def handle(self, *args, **options):
        path = Path(options["file_path"]).expanduser()
        if not path.exists():
            raise CommandError(f"Dataset file not found: {path}")

        suffix = path.suffix.lower()
        if suffix == ".csv":
            df = pd.read_csv(path)
        elif suffix in {".xlsx", ".xls"}:
            df = pd.read_excel(path)
        else:
            raise CommandError(f"Unsupported file extension '{suffix}'. Expected .csv, .xlsx, or .xls.")

        self.stdout.write(self.style.SUCCESS(f"Dataset: {path.name}"))
        self.stdout.write(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")

        self.stdout.write("=== Columns, Dtypes, Nulls, Unique Counts ===")
        summary_rows = []
        for col in df.columns:
            null_count = int(df[col].isna().sum())
            unique_count = int(df[col].nunique(dropna=True))
            sample_vals = ""
            if unique_count <= 12:
                vals = [str(v) for v in df[col].dropna().unique()[:8]]
                sample_vals = ", ".join(vals)
            summary_rows.append(
                {
                    "column": str(col),
                    "dtype": str(df[col].dtype),
                    "nulls": null_count,
                    "unique": unique_count,
                    "low_cardinality_values": sample_vals,
                }
            )
        self.stdout.write(pd.DataFrame(summary_rows).to_string(index=False))

        numeric_df = df.select_dtypes(include="number")
        if not numeric_df.empty:
            self.stdout.write("\n=== Numeric Summary ===")
            self.stdout.write(numeric_df.describe().round(2).to_string())

        self.stdout.write("\n=== First 5 Rows ===")
        self.stdout.write(df.head(5).to_string(index=False))
