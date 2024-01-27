# File: tests/test_word_api.py

from app.word_api import WordAPI

def test_get_word():
    word_api = WordAPI()
    result = word_api.get()
    assert "word" in result
    assert "definition" in result
