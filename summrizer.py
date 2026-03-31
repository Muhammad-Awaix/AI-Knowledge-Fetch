from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from fetcher import fetch_ai_news
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_article(title, summary):
    if not summary or summary == "No summary available":
        return "No content available to summarize. Click the link to read more."
    
    prompt = f"Summarize the following article in 3 simple and clear bullet points:\n\nTitle: {title}\nSummary: {summary}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()

if __name__ == "__main__":
    ai_news = fetch_ai_news()
    for article in ai_news:
        result = summarize_article(article["title"], article["summary"])
        print(f"Title: {article['title']}")
        print(f"Summary: {result}")
        print()