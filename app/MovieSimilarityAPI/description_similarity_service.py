import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from rake_nltk import Rake

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

class DescriptionSimilarityService:
    def __init__(self):
        # Load movie data from CSV file
        self.movies_df = pd.read_csv('similarity_model_dataset.csv')
        self.rake = Rake()
        # Create a bag-of-words representation for each movie description
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.movies_df['Description Tokenized'])
        self.movie_bow = self.vectorizer.fit_transform(self.movies_df['Description Tokenized'])

    def get_top_five_movies(self, user_input):
        # Tokenize and preprocess user input
        self.rake.extract_keywords_from_text(user_input)
        user_input_keywords = self.rake.get_ranked_phrases()
        user_input_tfidf = self.vectorizer.transform(user_input_keywords)

        # Calculate similarity between user input description and each movie description
        similarity_scores = cosine_similarity(user_input_tfidf, self.movie_bow)

        # Add a new column to movies_df with the similarity scores
        self.movies_df = self.movies_df.assign(similarity=similarity_scores[0])

        # Sort movies based on similarity score and return top 5
        ranked_movies = self.movies_df.sort_values('similarity', ascending=False)
        top_five_movies = ranked_movies.head(5)
        return top_five_movies['Name'].tolist()
    
    def get_description(self, movie_name):
        row = self.movies_df.loc[self.movies_df['Name'] == movie_name]
        print(row)
        if len(row) == 0:
            return None
        else:
            return row.iloc[0]['Description']
