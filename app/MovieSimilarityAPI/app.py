from flask import Flask, jsonify, request
from description_similarity_service import DescriptionSimilarityService
from category_predictor_service import CategoryPredictorService
from PyMovieDb import IMDB
import json

app = Flask(__name__)
movie_service = DescriptionSimilarityService()
category_predictor = CategoryPredictorService()
imdb = IMDB()

@app.route('/movies/top-five', methods=['POST'])
def get_top_five_movies():
    user_data = request.get_json()
    user_input = user_data['description']
    top_five_movies = movie_service.get_top_five_movies(user_input)
    response = []
    for movie in top_five_movies:
        movie_imdb = json.loads(imdb.get_by_name(movie.strip()))
        try:
            movie_response = {
                "name": movie_imdb["name"],
                "date published": movie_imdb["datePublished"],
                "description": movie_imdb["description"],
                "poster_url": movie_imdb["poster"],
                "imdb_url": movie_imdb["url"]
            }
            response.append(movie_response)
        except:
            pass
    return jsonify({'movies': response})

@app.route('/movies/predictgenre', methods=['POST'])
def predict():
    user_data = request.get_json()
    user_input = user_data['description']
    # Get model predictions for input text using the CategoryPredictorService
    predictions = category_predictor.predict(user_input)
    print(predictions)
    # Extract top predicted genres from dictionary of predictions
    top_genres = [genre for genre, prob in predictions.items() if prob >= 0.5]
    # Create JSON object with top predicted genres
    response = {
        "genres": top_genres
    }
    # Return JSON response with top predicted genres
    return jsonify(response)
