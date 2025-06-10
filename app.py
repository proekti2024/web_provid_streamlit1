import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scraper import scrape_quotes


st.set_page_config(page_title="Веб Провид", layout="wide")

st.title("📚 Веб Провид: Scraping Книги")
st.markdown("Оваа апликација врши автоматско вадење на книги од [books.toscrape.com](http://books.toscrape.com)")

pages = st.slider("Избери број на страници за scraping:", 1, 10, 3)

if st.button("📥 Изврши Scraping"):
    with st.spinner("Собирам податоци..."):
        df = scrape_books(pages)
        st.success(f"Пронајдени {len(df)} книги.")

        # Табела
        st.subheader("📊 Табела со книги")
        st.dataframe(df)

        # Бар график по Rating
        st.subheader("📈 Број на книги по рејтинг")
        fig, ax = plt.subplots()
        df['Rating'].value_counts().plot(kind='bar', ax=ax, color='skyblue')
        ax.set_xlabel("Рејтинг")
        ax.set_ylabel("Број на книги")
        st.pyplot(fig)

        # Хистограм на цени
        st.subheader("💰 Распределба на цени")
        fig2, ax2 = plt.subplots()
        df['Price (£)'].plot(kind='hist', bins=10, color='lightgreen', edgecolor='black', ax=ax2)
        ax2.set_xlabel("Цена во фунти")
        st.pyplot(fig2)
