# Tableau Handoff Guide

Use the CSV files in this folder to build a Tableau dashboard from the cleaned Netflix dataset.

## Generated Files

- `netflix_titles_clean.csv`: the cleaned title-level extract
- `type_distribution.csv`: Movies vs TV Shows summary
- `type_distribution_by_year.csv`: yearly type mix
- `top_genres.csv`: most common genres
- `genre_trend_by_year.csv`: genre trends by release year
- `top_countries.csv`: top producing countries
- `country_trend_by_year.csv`: country trends by release year
- `yearly_growth.csv`: titles added per year
- `monthly_growth.csv`: titles added per month

## Recommended Tableau Sheets

1. Content mix donut or bar chart from `type_distribution.csv`.
2. Type trend line chart from `type_distribution_by_year.csv`.
3. Top genres bar chart from `top_genres.csv`.
4. Genre trend heatmap or line chart from `genre_trend_by_year.csv`.
5. Top countries bar chart from `top_countries.csv`.
6. Country trend line chart from `country_trend_by_year.csv`.
7. Yearly growth line chart from `yearly_growth.csv`.
8. Monthly growth line chart from `monthly_growth.csv`.

## Suggested Dashboard Layout

- Top row: content type mix and yearly growth
- Middle row: top genres and top countries
- Bottom row: genre trend and country trend

## How To Use

1. Run `python scripts/export_tableau_data.py`.
2. Open Tableau Desktop.
3. Connect to the CSV files in `outputs/tableau/`.
4. Build each worksheet and combine them into a dashboard.

## Notes

If `data/netflix_titles.csv` is missing, the export script downloads the dataset from KaggleHub first and stores a local copy in `data/`.
