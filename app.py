import streamlit as st
from summrizer import summarize_article
from fetcher import fetch_ai_news

st.title("AI News Summarizer")
st.write("Fetching the latest AI news and summarizing it using Groq LLM...")

if st.button("Fetch and Summarize"):
    with st.spinner("Fetching and summarizing articles..."):
        articles = fetch_ai_news()
        
        # take only top 5
        articles = articles[:5]
        
        for article in articles:
            summary = summarize_article(article["title"], article["summary"])
            with st.container(border=True):
                st.subheader(article["title"])
                st.caption(article["date"])
                st.markdown(summary)
                st.markdown(f"[Read full article]({article['link']})")