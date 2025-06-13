import nltk

def download_nltk_resources():
    """
    Downloads necessary NLTK resources for tokenization, stopwords, lemmatization, and POS tagging.
    This function is intended to be run once to set up the environment.
    """
    # For tokenization and stopwords
    nltk.download('punkt')
    nltk.download('stopwords')


    # For lemmatization and POS tagging
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('averaged_perceptron_tagger_eng')