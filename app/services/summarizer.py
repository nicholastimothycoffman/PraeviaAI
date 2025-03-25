import os
import openai
from typing import Dict
from dotenv import load_dotenv

# Load API key from .env or environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_article(article: Dict) -> Dict:
	"""
	Uses OpenAI GPT to generate a summary, extract topics, and classify importance.
	Returns the enriched article dictionary.
	"""
	prompt = f"""
You are an AI research assistant. An article was fetched from {article.get('source')} titled:
"{article.get('title')}".

Here is the article summary:
\"\"\"
{article.get('summary')}
\"\"\"

Based on this, do the following:
1. Write a one-paragraph summary suitable for a weekly AI digest.
2. Extract 2-4 relevant tags (e.g., 'LangChain', 'RAG', 'OpenAI', 'LLMs').
3. Classify the article's importance using one of the following categories:
	[trivial, minor, significant, breakthrough].

Respond in this JSON format:
{{
	"llm_summary": "...",
	"tags": ["...", "..."],
	"importance": "..."
}}
"""

	try:
		response = openai.ChatCompletion.create(
			model="gpt-4",
			messages=[
				{"role": "system", "content": "You are an expert AI news summarizer."},
				{"role": "user", "content": prompt}
			],
			temperature=0.3,
		)

		# Extract structured JSON from LLM output
		content = response['choices'][0]['message']['content']

		# Use eval cautiously (or better: json.loads if format guaranteed)
		enriched_data = eval(content)

		# Merge results into article
		article.update(enriched_data)
		return article

	except Exception as e:
		print(f"OpenAI API error: {e}")
		return article
