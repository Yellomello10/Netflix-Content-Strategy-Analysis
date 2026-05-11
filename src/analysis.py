from __future__ import annotations

import pandas as pd

from .cleaning import explode_multi_value_column


def get_type_distribution(df: pd.DataFrame) -> pd.DataFrame:
    distribution = (
        df["type"].dropna().value_counts().rename_axis("type").reset_index(name="count")
    )
    distribution["percentage"] = distribution["count"] / distribution["count"].sum() * 100
    return distribution


def get_type_distribution_by_year(df: pd.DataFrame) -> pd.DataFrame:
    yearly = (
        df.dropna(subset=["release_year", "type"])
        .groupby(["release_year", "type"])
        .size()
        .reset_index(name="count")
        .sort_values(["release_year", "type"])
    )
    return yearly


def get_top_genres(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    exploded = explode_multi_value_column(df, "listed_in")
    genres = (
        exploded["listed_in"].value_counts().head(top_n).rename_axis("genre").reset_index(name="count")
    )
    return genres


def get_genre_trend(df: pd.DataFrame, top_n: int = 8) -> pd.DataFrame:
    exploded = explode_multi_value_column(df.dropna(subset=["release_year"]), "listed_in")
    top_genres = exploded["listed_in"].value_counts().head(top_n).index
    trend = (
        exploded[exploded["listed_in"].isin(top_genres)]
        .groupby(["release_year", "listed_in"])
        .size()
        .reset_index(name="count")
        .pivot(index="release_year", columns="listed_in", values="count")
        .fillna(0)
        .sort_index()
    )
    return trend


def get_top_countries(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    exploded = explode_multi_value_column(df, "country")
    countries = (
        exploded["country"].value_counts().head(top_n).rename_axis("country").reset_index(name="count")
    )
    return countries


def get_country_trend(df: pd.DataFrame, top_n: int = 8) -> pd.DataFrame:
    exploded = explode_multi_value_column(df.dropna(subset=["release_year"]), "country")
    top_countries = exploded["country"].value_counts().head(top_n).index
    trend = (
        exploded[exploded["country"].isin(top_countries)]
        .groupby(["release_year", "country"])
        .size()
        .reset_index(name="count")
        .pivot(index="release_year", columns="country", values="count")
        .fillna(0)
        .sort_index()
    )
    return trend


def get_growth_trends(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    yearly = (
        df.dropna(subset=["added_year"])
        .groupby("added_year")
        .size()
        .sort_index()
    )
    monthly = (
        df.dropna(subset=["added_month"])
        .groupby("added_month")
        .size()
        .sort_index()
    )
    return yearly, monthly


def summarize_content_focus(df: pd.DataFrame) -> dict[str, object]:
    type_distribution = get_type_distribution(df)
    type_counts = type_distribution.set_index("type")["count"].to_dict()
    type_pct = type_distribution.set_index("type")["percentage"].round(1).to_dict()
    top_genres = get_top_genres(df, top_n=3)
    top_countries = get_top_countries(df, top_n=3)

    return {
        "type_counts": type_counts,
        "type_percentages": type_pct,
        "top_genres": top_genres.to_dict(orient="records"),
        "top_countries": top_countries.to_dict(orient="records"),
        "years_covered": {
            "release_year_min": int(df["release_year"].min()) if "release_year" in df and df["release_year"].notna().any() else None,
            "release_year_max": int(df["release_year"].max()) if "release_year" in df and df["release_year"].notna().any() else None,
            "added_year_min": int(df["added_year"].min()) if "added_year" in df and df["added_year"].notna().any() else None,
            "added_year_max": int(df["added_year"].max()) if "added_year" in df and df["added_year"].notna().any() else None,
        },
    }
