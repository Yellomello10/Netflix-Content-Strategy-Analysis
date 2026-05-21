import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "tableau"
TWB_PATH = OUTPUT_DIR / "netflix_dashboard.twb"

CSV_FILES = [
    ("netflix_titles_clean.csv", "Netflix Titles (Clean)"),
    ("type_distribution.csv", "Type Distribution"),
    ("type_distribution_by_year.csv", "Type Distribution by Year"),
    ("top_genres.csv", "Top Genres"),
    ("genre_trend_by_year.csv", "Genre Trend by Year"),
    ("top_countries.csv", "Top Countries"),
    ("country_trend_by_year.csv", "Country Trend by Year"),
    ("yearly_growth.csv", "Yearly Growth"),
    ("monthly_growth.csv", "Monthly Growth"),
]

def generate_twb_xml() -> str:
    xml_header = """<?xml version='1.0' encoding='utf-8' ?>
<workbook source-build='2020.4.0 (20204.20.1106.0321)' source-platform='win' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
  <document-format-change-manifest>
    <AutoCreateAndUpdateDseBindings flag='true' />
    <SchemaRenderingDbConnections flag='true' />
    <SharedXmlProperties flag='true' />
  </document-format-change-manifest>
  <preferences>
  </preferences>
  <datasources>"""

    xml_datasources = []
    for filename, caption in CSV_FILES:
        name_id = filename.replace(".csv", "")
        # Escaped names for XML
        table_name = f"[{name_id}#csv]"
        
        datasource_xml = f"""
    <datasource caption='{caption}' inline='true' name='federated.{name_id}' version='18.1'>
      <connection class='federated'>
        <named-connections>
          <named-connection caption='{caption}' name='textscan.{name_id}'>
            <connection class='textscan' directory='.' filename='{filename}' format='local' name='textscan.{name_id}' />
          </named-connection>
        </named-connections>
        <relation connection='textscan.{name_id}' name='{filename}' table='{table_name}' type='table' />
      </connection>
      <layout dim-ordering='alphabetic' dim-percentage='0.5' measure-ordering='alphabetic' measure-percentage='0.5' show-structure='true' />
      <semantic-values>
        <semantic-value key='[Country].[Name]' value='&quot;United States&quot;' />
      </semantic-values>
    </datasource>"""
        xml_datasources.append(datasource_xml)

    xml_footer = """
  </datasources>
  <worksheets>
    <worksheet name='Sheet 1'>
      <table>
        <view>
          <datasources />
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane />
        </panes>
        <rows />
        <cols />
      </table>
    </worksheet>
  </worksheets>
  <windows>
    <window class='worksheet' name='Sheet 1'>
      <active />
    </window>
  </windows>
</workbook>
"""

    return xml_header + "".join(xml_datasources) + xml_footer

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    twb_content = generate_twb_xml()
    
    with open(TWB_PATH, "w", encoding="utf-8") as f:
        f.write(twb_content)
        
    print(f"Tableau Workbook template successfully created at: {TWB_PATH}")

if __name__ == "__main__":
    main()
