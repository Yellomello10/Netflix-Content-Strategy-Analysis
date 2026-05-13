# Netflix Content Strategy Analysis Summary

## Dataset
- Source file: `data/netflix_titles.csv`
- Analysis date: 2026-05-13

## Executive Summary
- Netflix's catalog is movie-first, with a strong strategic push into international productions and drama. The platform's largest catalog expansion occurred in 2019, with elevated monthly additions continuing into 2020–2021 driven by both US and international production growth.

## Movies vs TV Shows
- Total movies: 6,131
- Total TV shows: 2,676
- Share of movies: 69.6%
- Share of TV shows: 30.4%
- Interpretation: The catalog is dominated by movies, suggesting Netflix prioritizes volume and international movie licensing/production while still investing in TV series growth.

## Genre Trends
- Top genres:
	- International Movies: 2,752 titles
	- Dramas: 2,427 titles
	- Comedies: 1,674 titles
- Notable genre shifts over time: A marked increase in "International Movies" and "Dramas" from 2016 onward.
- Interpretation: Netflix doubled down on internationally produced movies and prestige drama, supporting both global subscriber acquisition and local-market relevance.

## Country Production
- Top producing countries:
	- United States: 3,690 titles
	- India: 1,046 titles
	- United Kingdom: 806 titles
- Countries with fastest recent growth: India shows accelerated additions after 2016; other non-US markets also scale from 2016–2019.
- Interpretation: US remains dominant, but strategic investment in India and other international markets is clear—aligning with localization and global expansion objectives.

## Growth Over Time
- Year with the largest catalog expansion: 2019 (1,999 titles added)
- Month with the largest additions: 2021-07 (257 titles added)
- Interpretation: Rapid scaling occurred 2016–2019 with a 2019 peak; monthly activity remained high into 2020–2021, indicating sustained content acquisition/production even as yearly cadence normalized.

## Strategic Takeaways
- Focus: High-volume movie acquisition/production, especially international movies and dramas.
- Global expansion: Heavy investment in India and other local markets since 2016.
- Product strategy signal: A mix of volume (movies) and marquee series (dramas) to drive both discovery and retention.

## Deliverables
- Charts saved in `outputs/charts/` (9 PNGs: type, genres, countries, growth)
- Tableau-ready CSVs in `outputs/tableau/` (type_distribution, genre_trend_by_year, country_trend_by_year, yearly_growth, monthly_growth, etc.)
- Notebook: `notebooks/analysis.ipynb`

## Quick Tableau Dashboard Instructions
- Open Tableau Desktop 26.1.1 and connect to the CSV files in `outputs/tableau/`.
- Recommended sheets:
	- Donut chart: type_distribution.csv
	- Stacked/line charts: type_distribution_by_year.csv and genre_trend_by_year.csv
	- Heatmap: genre_trend_by_year.csv (genres × release year)
	- Country trend lines: country_trend_by_year.csv
	- Yearly and monthly growth line charts: yearly_growth.csv and monthly_growth.csv
- Layout suggestion: top row - headline KPIs and type donut; middle row - genre heatmap + top genres; bottom row - country trends + growth lines.

## Next Steps (optional)
- Build Tableau workbook scaffolding (ask me to create a `.twb` starter file or a step-by-step worksheet script).
- Commit final reports and charts to the repo if you want them versioned.
