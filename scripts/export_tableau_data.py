from __future__ import annotations

from pathlib import Path
import shutil
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analysis import (
    get_country_trend,
    get_growth_trends,
    get_genre_trend,
    get_top_countries,
    get_top_genres,
    get_type_distribution,
    get_type_distribution_by_year,
)
from src.cleaning import clean_netflix_titles, load_netflix_titles, validate_netflix_schema


DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "tableau"
CSV_NAME = "netflix_titles.csv"


def ensure_source_dataset() -> Path:
    source_path = DATA_DIR / CSV_NAME
    if source_path.exists():
        return source_path

    try:
        import kagglehub
    except ImportError as exc:  # pragma: no cover - install issue is environment-specific
        raise ImportError(
            "kagglehub is required to download the Netflix dataset. Install the project dependencies first."
        ) from exc

    downloaded_path = Path(kagglehub.dataset_download("shivamb/netflix-shows"))
    csv_candidates = sorted(downloaded_path.rglob("*.csv"))
    if not csv_candidates:
        raise FileNotFoundError(f"No CSV files were found in {downloaded_path}.")

    source_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(csv_candidates[0], source_path)
    return source_path


def export_tableau_extracts(df: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_DIR / "netflix_titles_clean.csv", index=False)
    get_type_distribution(df).to_csv(OUTPUT_DIR / "type_distribution.csv", index=False)
    get_type_distribution_by_year(df).to_csv(OUTPUT_DIR / "type_distribution_by_year.csv", index=False)
    get_top_genres(df, top_n=10).to_csv(OUTPUT_DIR / "top_genres.csv", index=False)
    get_genre_trend(df, top_n=8).reset_index().to_csv(OUTPUT_DIR / "genre_trend_by_year.csv", index=False)
    get_top_countries(df, top_n=10).to_csv(OUTPUT_DIR / "top_countries.csv", index=False)
    get_country_trend(df, top_n=8).reset_index().to_csv(OUTPUT_DIR / "country_trend_by_year.csv", index=False)

    yearly_growth, monthly_growth = get_growth_trends(df)
    yearly_growth.rename("count").reset_index().to_csv(OUTPUT_DIR / "yearly_growth.csv", index=False)
    monthly_growth.rename("count").reset_index().to_csv(OUTPUT_DIR / "monthly_growth.csv", index=False)


def main() -> None:
    source_path = ensure_source_dataset()
    raw_df = load_netflix_titles(source_path)
    cleaned_df = validate_netflix_schema(clean_netflix_titles(raw_df))
    export_tableau_extracts(cleaned_df)
    print(f"Source dataset: {source_path}")
    print(f"Tableau extracts written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
