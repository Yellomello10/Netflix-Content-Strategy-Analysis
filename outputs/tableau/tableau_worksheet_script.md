Tableau Worksheet Script — Netflix Content Strategy Dashboard

Prerequisites
- Tableau Desktop 26.1.1 installed
- CSV extracts located in `outputs/tableau/` inside the project root
- Files used: `netflix_titles_clean.csv`, `type_distribution.csv`, `type_distribution_by_year.csv`, `top_genres.csv`, `genre_trend_by_year.csv`, `top_countries.csv`, `country_trend_by_year.csv`, `yearly_growth.csv`, `monthly_growth.csv`

Overview
This script walks through creating nine Tableau sheets and assembling them into a single dashboard. Follow steps in order.

1) Data connection
- Open Tableau Desktop.
- From the start page choose "Text File" and navigate to `outputs/tableau/netflix_titles_clean.csv`.
- After loading, click "Add" -> "Text File" for the other CSVs, or use "Data" -> "New Data Source" for each file.
- For convenience, rename each data source exactly as the file name (e.g., `type_distribution`).

2) Sheet: `Type Donut` (type_distribution.csv)
- New Worksheet -> rename `Type Donut`.
- Connect to `type_distribution.csv`.
- Drag `type` to Rows.
- Drag `count` to Angle and to Label.
- Create a calculated field `Percent` = `count` / TOTAL(SUM([count])) * 100 and format as percentage with 1 decimal.
- On Marks card set to Pie; drag `count` to Angle and `type` to Color.
- Add `Percent` to Label and format.
- To make a donut: create a dual-axis with a white circle in the center: duplicate the pie, change inner mark to a circle with white color and adjust sizes; hide headers.
- Caption: "Movies vs TV Shows — share of catalog".

3) Sheet: `Type Trend` (type_distribution_by_year.csv)
- New Worksheet -> `Type Trend`.
- Connect to `type_distribution_by_year.csv`.
- Drag `release_year` to Columns (continuous, Year). Drag `count` to Rows.
- Drag `type` to Color.
- Change mark to Line and smooth if desired.
- Add table calculation `% of Total` if you want relative share over time.

4) Sheet: `Top Genres` (top_genres.csv)
- New Worksheet -> `Top Genres`.
- Connect to `top_genres.csv`.
- Drag `genre` to Rows, `count` to Columns.
- Sort descending by `count` and limit to top N (use filter Top N if needed).
- Use horizontal bar chart, show labels with counts.

5) Sheet: `Genre Trends` (genre_trend_by_year.csv)
- New Worksheet -> `Genre Trends`.
- Connect to `genre_trend_by_year.csv`.
- Drag `release_year` to Columns (continuous), `count` to Rows.
- Drag `genre` to Color and to Detail if many genres; filter to Top 8 genres (use a set or Top N filter based on `top_genres.csv`).
- Mark type: Line.
- Consider adding parameter to choose Top N genres interactively.

6) Sheet: `Genre Heatmap` (genre_trend_by_year.csv)
- New Worksheet -> `Genre Heatmap`.
- Connect to `genre_trend_by_year.csv`.
- Drag `genre` to Rows, `release_year` to Columns.
- Drag `count` to Color; change color palette to sequential (Reds) and set center to low values.
- Adjust cell sizing to square-ish shape; add labels if space permits.

7) Sheet: `Top Countries` (top_countries.csv)
- New Worksheet -> `Top Countries`.
- Connect to `top_countries.csv`.
- Drag `country` to Rows, `count` to Columns.
- Sort descending, horizontal bars, show count labels.

8) Sheet: `Country Trends` (country_trend_by_year.csv)
- New Worksheet -> `Country Trends`.
- Connect to `country_trend_by_year.csv`.
- Drag `release_year` to Columns, `count` to Rows, `country` to Color.
- Filter to Top 8 countries (use `top_countries.csv` for the list).
- Use Line marks; add tooltips with country and year count.

9) Sheet: `Yearly Growth` (yearly_growth.csv)
- New Worksheet -> `Yearly Growth`.
- Connect to `yearly_growth.csv`.
- Drag `added_year` to Columns (continuous), `count` to Rows.
- Use Line with markers; annotate the peak year (2019) using an annotation.

10) Sheet: `Monthly Growth` (monthly_growth.csv)
- New Worksheet -> `Monthly Growth`.
- Connect to `monthly_growth.csv`.
- Convert `added_month` to a date: create calculated field `AddedMonthDate` = DATEPARSE("yyyy-MM", [added_month]) (or parse in Excel if Tableau's DATEPARSE not available).
- Drag `AddedMonthDate` to Columns, `count` to Rows.
- Use Line; set axis to continuous months; add a rolling average table calculation (3 or 6 months) to smooth seasonality.

11) Build Dashboard
- New Dashboard -> set size to 1400x900 or Dashboard -> Automatic.
- Layout suggestion:
  - Top row (full width): KPI text box showing totals (Movies, TV Shows) and `Type Donut` on the right.
  - Middle row (split): Left: `Genre Heatmap` (wider); Right: `Top Genres` stacked above `Genre Trends`.
  - Bottom row (split): Left: `Country Trends`; Right: `Top Countries` above `Yearly Growth` and `Monthly Growth` stacked.
- Add filters: `release_year` and `genre` as global filters. Allow single-select for genre and multi-select for countries.
- Add a parameter for `Top N` to control top genres/countries displayed.

12) Tooltips and formatting
- Standardize fonts and colors to Netflix palette: primary red `#e50914`, dark background `#221f1f`, light text.
- For all charts, enable hover tooltips that show exact counts and percentages where relevant.

13) Export and sharing
- Save workbook: `File` -> `Save As` -> choose `.twb` (workbook) or `.twbx` (packaged) if you want to embed data.
- To publish to Tableau Server: `Server` -> `Publish Workbook` and follow your org settings.

14) Optional: Automation / Refresh
- If you plan to refresh CSVs regularly, save the workbook using relative paths and use Tableau Bridge or schedule a refresh on Tableau Server.

Notes & Tips
- Use the CSVs in `outputs/tableau/` as the single source of truth; if you re-run the export script, the workbook will pick up new data if saved with relative links.
- If `DATEPARSE` fails for `monthly_growth.csv`, create an Excel column converting `YYYY-MM` to an ISO date, or create a calculated field splitting year/month and using `MAKEDATE()`.

End of script. Follow these steps interactively in Tableau to build the dashboard. If you want, I can generate a minimal `.twb` XML file that points to the CSVs using relative paths (Windows) — say "generate .twb" and I'll scaffold it for you.
