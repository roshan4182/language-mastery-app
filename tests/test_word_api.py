# File: tests/test_word_api.py

import unittest
from unittest.mock import patch, Mock
from app.word_api import WordAPI
from test_main import TestLearnWordApp

class TestLearnWordApp(unittest.TestCase):
    def test_get_word():
        word_api = WordAPI()
        result = word_api.get()
        assert "word" in result
        assert "definition" in result
