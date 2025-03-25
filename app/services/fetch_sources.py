import feedparser
from datetime import datetime
from typing import List, Dict

def fetch_arxiv_articles(
	feed_url: str = "https://export.arxiv.org/rss/cs.AI",
	max_articles: int = 10
) -> List[Dict]:
	"""
	Fetches articles from the arXiv RSS feed for Artificial Intelligence.
	Returns a list of dictionaries with article metadata.
	"""
	feed = feedparser.parse(feed_url)
	articles = []

	for entry in feed.entries[:max_articles]:
		article = {
			"title": entry.title,
			"source": "arXiv",
			"url": entry.link,
			"published": entry.published,
			"summary": entry.summary,
			"fetched_at": datetime.utcnow().isoformat()
		}
		articles.append(article)
	
	return articles

# To test as a script
if __name__ == "__main__":
	articles = fetch_arxiv_articles()
	for a in articles:
		print(f"{a['published']} - {a['title']}\n{a['url']}\n")
