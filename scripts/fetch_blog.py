import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED_URL = "https://shizu2013.hatenablog.com/rss"
OUTPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "_site/blog.json"

request = urllib.request.Request(
    FEED_URL,
    headers={"User-Agent": "Shizu2013-Portfolio/1.0"},
)

with urllib.request.urlopen(request, timeout=30) as response:
    root = ET.fromstring(response.read())

posts = []

for item in root.findall("./channel/item")[:5]:
    title = item.findtext("title", default="").strip()
    url = item.findtext("link", default="").strip()
    published = item.findtext("pubDate", default="").strip()

    try:
        date = parsedate_to_datetime(published).date().isoformat()
    except (TypeError, ValueError):
        date = published

    if title and url:
        posts.append({
            "title": title,
            "url": url,
            "date": date,
        })

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(posts, file, ensure_ascii=False, indent=2)
