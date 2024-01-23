# app/word_api/word_api.py

import sys
sys.path.append('/Users/roshan1610/Desktop/language-mastery-app/app')
from flask_restful import Resource
from shared.words_api_logic import get_word_data

class WordAPI(Resource):
    def get(self):
        word_data = get_word_data()
        return {"word": word_data["word"], "meaning": word_data["meaning"]}
