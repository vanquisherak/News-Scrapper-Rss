# 🌍 News Scraper from RSS Feeds

A Python-based news scraping tool that collects and processes global news headlines and summaries from RSS feeds across multiple countries. The tool stores the results in both JSON and CSV formats and detects the language of each news item.

---

## 📦 Project Structure

```
news_scraper_rss/
│
├── rss_feeds.json               # Country-wise list of RSS feed URLs
├── news_scraper.py              # Main Python script to run the scraper
├── requirements.txt             # Python dependencies
├── output/
│   ├── news_data.json           # Output file (JSON format)
│   └── news_data.csv            # Output file (CSV format)
├── README.md                    # Project documentation (you are here)
└── utils/
    └── helpers.py               # Utility functions for cleaning and language detection
```

---

## 🚀 Features

- 🌐 Scrapes RSS feeds from 20+ countries  
- 🧹 Cleans and normalizes news content  
- 🌍 Detects the language of each news headline  
- 📁 Saves output in both CSV and JSON formats  
- ✅ Easy to extend with new feeds or processing logic  

---

## 🛠️ Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `feedparser`
- `pandas`
- `langdetect`

---

## 📥 How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/news_scraper_rss.git
   cd news_scraper_rss
   ```

2. **Add/Update RSS feeds:**

   Edit `rss_feeds.json` to include new RSS URLs under their respective countries.

3. **Run the scraper:**

   ```bash
   python news_scraper.py
   ```

4. **Check outputs:**

   Results will be saved in the `output/` folder:
   - `news_data.csv`
   - `news_data.json`

---

## 🔍 Sample Output

Each news item contains:

```json
{
  "title": "India's space program launches new satellite",
  "summary": "The satellite is expected to improve communication services.",
  "published": "Mon, 20 May 2025 08:00:00 GMT",
  "link": "https://timesofindia.indiatimes.com/...",
  "source": "timesofindia.indiatimes.com",
  "country": "India",
  "language": "en"
}
```

---

## 🧠 How It Works

- `news_scraper.py`: Main script that loads RSS feeds, fetches and parses articles, and stores output.
- `helpers.py`: Utility functions to clean text and detect the language of article titles using `langdetect`.

---

## 🧪 Optional Enhancements

- Add support for scheduling via `cron` or `APScheduler`
- Integrate Flask/Django to serve results via API
- Store data in a database (e.g., SQLite, PostgreSQL)
- Add keyword filters, categories, or sentiment analysis

---

## 📄 License

MIT License. See `LICENSE` for more information.

---

## 🙌 Acknowledgements

- [Feedparser](https://pythonhosted.org/feedparser/)
- [Langdetect](https://pypi.org/project/langdetect/)
- [Pandas](https://pandas.pydata.org/)

---

## 👨‍💻 Author

**Ankit Kushwaha**  
[My GitHub Profile](https://github.com/vanquisherak)