import streamlit as st
from scraper import scrape_books

st.set_page_config(page_title="Books Scraper", layout="centered")
st.title("📚 Books to Scrape Viewer")

st.markdown("Избери број на страници за скенирање (1 до 10)")

max_pages = st.slider("Број на страници:", 1, 10, 3)

if st.button("🔍 Scrape Books"):
    with st.spinner("Собирам информации за книги..."):
        results = scrape_books(max_pages)
    st.success(f"Пронајдени книги: {len(results)}")
    for book in results:
        st.markdown(book)
