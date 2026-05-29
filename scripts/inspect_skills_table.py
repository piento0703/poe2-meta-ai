from pathlib import Path
from bs4 import BeautifulSoup

HTML_PATH = Path("data/skills/skill_gems.html")

html = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
soup = BeautifulSoup(html, "lxml")

tables = soup.find_all("table")

print(f"table 개수: {len(tables)}")
print("=" * 100)

for i, table in enumerate(tables[:20]):
    text = table.get_text("\n", strip=True)
    print(f"\nTABLE #{i}")
    print("-" * 100)
    print(text[:1500])