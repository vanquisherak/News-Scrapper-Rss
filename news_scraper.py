import json
import feedparser
import pandas as pd
from utils.helpers import clean_text, detect_language
from datetime import datetime
import os

def load_feeds(file_path='rss_feeds.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

def parse_feed(feed_url, country, agency):
    feed = feedparser.parse(feed_url)
    entries = []
    for entry in feed.entries:
        entries.append({
            "title": clean_text(entry.get("title", "")),
            "summary": clean_text(entry.get("summary", entry.get("description", ""))),
            "published": entry.get("published", ""),
            "link": entry.get("link", ""),
            "source": agency,
            "country": country,
            "language": detect_language(entry.get("title", ""))
        })
    return entries

def main():
    feeds = load_feeds()
    all_entries = []

    for country, urls in feeds.items():
        for url in urls:
            print(f"Fetching: {url} for {country}")
            agency = url.split("//")[1].split("/")[0]
            try:
                entries = parse_feed(url, country, agency)
                all_entries.extend(entries)
            except Exception as e:
                print(f"Failed {url}: {e}")

    df = pd.DataFrame(all_entries)
    os.makedirs("output", exist_ok=True)
    df.to_csv("output/news_data.csv", index=False, encoding="utf-8")
    df.to_json("output/news_data.json", orient="records", indent=2, force_ascii=False)

if __name__ == "__main__":
    main()
