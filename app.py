import os
import sys
import pickle
import streamlit as st
import numpy as np
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline

class BookRecommendation:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.recommendation_config = app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys) from e
        
    def fetch_poster(self, suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            final_rating = pickle.load(open(self.recommendation_config.final_rating_serialized_objects, 'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])
            
            for name in book_name[0]:
                ids = np.where(final_rating['title'] == name)[0][0]
                ids_index.append(ids)
            
            for idx in ids_index:
                url = final_rating.iloc[idx]['image_url']
                poster_url.append(url)

            return poster_url
        
        except Exception as e:
            raise AppException(e, sys) from e
        
    def recommend_books(self, book_name):
        try:
            books_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]
            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

            poster_url = self.fetch_poster(suggestion)

            for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    books_list.append(j)
            return books_list, poster_url
        
        except Exception as e:
            raise AppException(e, sys) from e
        
    def train_model(self):
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.text("✅ Training completed successfully!")
            logging.info("Recommendation model trained successfully.")

        except Exception as e:
            st.error("❌ Training failed. Check logs for details.")
            raise AppException(e, sys) from e
        
    def recommendation_engine(self, selected_books):
        try:
            recommended_books, poster_url = self.recommend_books(selected_books)
            st.markdown("---")
            st.subheader("📚 Recommended Books For You")
            cols = st.columns(5)
            for i in range(1, 6):
                with cols[i-1]:
                    st.image(poster_url[i], use_column_width=True)
                    st.markdown(
                        f"<div style='text-align: center; font-weight: bold; color: #4B8BBE;'>{recommended_books[i]}</div>",
                        unsafe_allow_html=True
                    )
        
        except Exception as e:
            st.error("❌ Could not fetch recommendations.")
            raise AppException(e, sys) from e
        

if __name__ == "__main__":
    st.set_page_config(page_title="ReadMind", page_icon="📖", layout="wide")
    st.markdown(
        "<h1 style='text-align: center; color: #4B8BBE;'>ReadMind</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size:18px;'>A Collaborative Filtering based <b>Book Recommendation System</b>.</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    obj = BookRecommendation()

    with st.sidebar:
        st.header("Actions")
        if st.button("🚀 Train Recommendation Engine"):
            obj.train_model()

    book_names = pickle.load(open(os.path.join('templates', 'book_names.pkl'), 'rb'))
    selected_books = st.selectbox("Type or select a book", book_names)

    if st.button("🔎 Show Recommendation"):
        obj.recommendation_engine(selected_books)