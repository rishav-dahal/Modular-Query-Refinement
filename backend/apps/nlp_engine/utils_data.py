from gensim import corpora, models
from core.settings.base import MODEL_DIR
def download_nltk_resources():
    """
    Downloads necessary NLTK resources for tokenization, stopwords, lemmatization, and POS tagging.
    This function is intended to be run once to set up the environment.
    """
    # For tokenization and stopwords
    # nltk.download('punkt')
    # nltk.download('stopwords')


    # # For lemmatization and POS tagging
    # nltk.download('wordnet')
    # nltk.download('omw-1.4')
    # nltk.download('averaged_perceptron_tagger_eng')

    #spacy 
    # spacy.cli.download("en_core_web_sm")
    # spacy.load("en_core_web_sm")

    # return "NLTK resources downloaded successfully."

def load_models():
    """
    Loads necessary NLP models and resources.
    
    
    """
    import os

    optimal_lda_model = os.path.join(MODEL_DIR, 'lda_model.model')
    optimal_lda_dict = os.path.join(MODEL_DIR, 'lda_dict.dict')
    optimal_model = models.LdaModel.load(optimal_lda_model)
    dictionary = corpora.Dictionary.load(optimal_lda_dict)

    return optimal_model, dictionary