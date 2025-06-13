import unittest

# Import your main functions from your modules
from utils_data import download_nltk_resources
from tokenization import tokenize_text
from lemmatization import lemmatize_word

class NLPUtilsIntegrationTest(unittest.TestCase):

    """
    Integration tests for NLP utilities.
    These tests ensure that the main functionalities of the NLP utilities work together as expected.
    """
    def test_download_nltk_resources(self):
        download_nltk_resources()
        
    def setUp(self):
        self.sample_text = "The striped bats are hanging on their feet for best."
        self.tokens = tokenize_text(self.sample_text)

    def test_tokenization(self):
        self.assertIsInstance(self.tokens, list)
        self.assertIn('striped', self.tokens)
        self.assertIn('bats', self.tokens)

    def test_lemmatization(self):
        lemmatized = lemmatize_word(self.tokens)
        self.assertIsInstance(lemmatized, list)
        self.assertIn('bat', lemmatized)    
        self.assertIn('hang', lemmatized)   


if __name__ == "__main__":
    unittest.main()