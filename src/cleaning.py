from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


COLUMN_RENAMES = {
    "show id": "show_id",
    "type": "type",
    "title": "title",
    "director": "director",
    "cast": "cast",
    "country": "country",
    "date added": "date_added",
    "release year": "release_year",
    "rating": "rating",
    "duration": "duration",
    "listed in": "listed_in",
    "description": "description",
}

REQUIRED_COLUMNS = {
    "type",
    "title",
    "country",
    "date_added",
    "release_year",
    "listed_in",
}


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    normalized.columns = [str(column).strip().lower() for column in normalized.columns]
    normalized = normalized.rename(columns={key: value for key, value in COLUMN_RENAMES.items() if key in normalized.columns})
    return normalized


def load_netflix_titles(csv_path: str | Path) -> pd.DataFrame:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(
            f"Could not find the Netflix dataset at {path}. Place netflix_titles.csv in the data/ folder first."
        )
    return pd.read_csv(path)


def validate_netflix_schema(df: pd.DataFrame) -> pd.DataFrame:
    missing_columns = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing_columns:
        raise ValueError(
            "The Netflix dataset is missing required columns: "
            f"{', '.join(missing_columns)}. Expected the standard Netflix titles schema."
        )
    return df


def clean_netflix_titles(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = normalize_columns(df)

    for column in ("date_added", "release_year"):
        if column not in cleaned.columns:
            continue

    if "date_added" in cleaned.columns:
        cleaned["date_added"] = pd.to_datetime(cleaned["date_added"], errors="coerce")
        cleaned["added_year"] = cleaned["date_added"].dt.year
        cleaned["added_month"] = cleaned["date_added"].dt.to_period("M").astype(str)

    if "release_year" in cleaned.columns:
        cleaned["release_year"] = pd.to_numeric(cleaned["release_year"], errors="coerce").astype("Int64")

    if "type" in cleaned.columns:
        cleaned["type"] = cleaned["type"].astype("string").str.strip()

    for column in ("country", "listed_in", "director", "cast", "rating", "duration"):
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].astype("string").str.strip()

    return cleaned


def explode_multi_value_column(df: pd.DataFrame, column: str, delimiter: str = ",") -> pd.DataFrame:
    if column not in df.columns:
        raise KeyError(f"Column '{column}' does not exist in the dataframe.")

    exploded = df.copy()
    exploded[column] = exploded[column].fillna("").astype(str).str.split(delimiter)
    exploded = exploded.explode(column)
    exploded[column] = exploded[column].astype(str).str.strip()
    exploded = exploded[exploded[column].ne("") & exploded[column].ne("nan")]
    return exploded


def prepare_netflix_dataset(csv_path: str | Path) -> pd.DataFrame:
    return validate_netflix_schema(clean_netflix_titles(load_netflix_titles(csv_path)))


def sample_preview(df: pd.DataFrame, columns: Iterable[str] | None = None) -> pd.DataFrame:
    preview_columns = list(columns) if columns else list(df.columns[:8])
    existing_columns = [column for column in preview_columns if column in df.columns]
    return df.loc[:, existing_columns].head(5)
