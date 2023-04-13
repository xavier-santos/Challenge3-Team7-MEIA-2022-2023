import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

class CategoryPredictorService:
    def __init__(self, model_path='LSTM_Basic', max_len=200):
        self.model = load_model(model_path)
        self.tokenizer = Tokenizer()
        self.max_len = max_len
        # Initialize tokenizer with dummy text
        self.tokenizer.fit_on_texts(['This is a dummy text'])
        self.category_names = ["Comedy", "Crime", "Drama", "Romance", "Action and Adventure", 
               "Documentary and History", "Family and Animation", "Fantasy and Sci-Fi", 
               "Horror and Thriller"]
        
    def predict(self, input_text):
        # Tokenize and pad input text
        sequences = self.tokenizer.texts_to_sequences([input_text])
        padded_sequences = pad_sequences(sequences, maxlen=self.max_len)

        # Get model predictions for input text
        predictions = self.model.predict(padded_sequences)[0]

        # Convert predictions to a dictionary of category names and probabilities
        category_probabilities = predictions.tolist()
        category_dict = dict(zip(self.category_names, category_probabilities))

        return category_dict
