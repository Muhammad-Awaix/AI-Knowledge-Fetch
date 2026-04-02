import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import email.utils

def is_recent(date_str, days=90):
    try:
        parsed = email.utils.parsedate_to_datetime(date_str)
        now = datetime.now(timezone.utc)
        diff = now - parsed
        return diff.days <= days
    except:
        return True

def clean_html(text):
    return BeautifulSoup(text, "html.parser").get_text()

def fetch_ai_news():
    feeds = [
    "https://venturebeat.com/category/ai/feed/",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://bdtechtalks.com/feed/",
    "https://blog.tensorflow.org/feeds/posts/default",
    "https://newsletter.theaiedge.io/feed",
]
    
    articles = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            date = entry.get("published", "")
            if not is_recent(date, days=30):
                continue
            raw = entry.get("summary", entry.get("description", ""))
            cleaned = clean_html(raw)[:500]
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": cleaned if cleaned.strip() else "No summary available",
                "date": date
            })
    return articles

if __name__ == "__main__":
    news = fetch_ai_news()
    print(f"Total articles found: {len(news)}")
    for a in news:
        print(a["date"], "-", a["title"])