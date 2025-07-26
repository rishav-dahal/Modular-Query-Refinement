from gensim import corpora, models
from gensim.models import LsiModel
import joblib
from sentence_transformers import SentenceTransformer
import os
from core.settings.base import MODEL_DIR
import json
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


    #LSA without verb
    lda_model_path = os.path.join(MODEL_DIR, 'lda_model.model')
    lda_dict_path = os.path.join(MODEL_DIR, 'lda_dict.dict')
    lda_model = models.LdaModel.load(lda_model_path)
    lda_dictionary = corpora.Dictionary.load(lda_dict_path)

    #LSI NAD LDA 
    lsi_model_path = os.path.join(MODEL_DIR, 'optimal_lsi_model.model')
    lsi_dict_path = os.path.join(MODEL_DIR, 'optimal_lsi_dict.dict')
    lsi_tfidf_path = os.path.join(MODEL_DIR, 'optimal_lsi_tfidf.model')
    lsi_model = LsiModel.load(lsi_model_path)
    lsi_dictionary = corpora.Dictionary.load(lsi_dict_path)
    lsi_tfidf_model = models.TfidfModel.load(lsi_tfidf_path)

    #LDA with verb
    optimal_lda_model_path = os.path.join(MODEL_DIR, 'optimal_lda_model.model')
    optimal_lda_dict_path = os.path.join(MODEL_DIR, 'optimal_lda_dict.dict')
    optimal_lda_model = models.LdaModel.load(optimal_lda_model_path)
    optimal_lda_dictionary = corpora.Dictionary.load(optimal_lda_dict_path)

    #BERT with kmeans
    bert_model_path = os.path.join(MODEL_DIR, 'kmeans_model.pkl')
    bert_model = joblib.load(bert_model_path)
    sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

    cluster_keywords_path = os.path.join(MODEL_DIR, "cluster_keywords.json")
    with open(cluster_keywords_path, "r") as f:
        cluster_keywords = json.load(f)


    return lda_model, lda_dictionary , lsi_model , lsi_dictionary, optimal_lda_model, optimal_lda_dictionary , lsi_tfidf_model , bert_model, cluster_keywords, sentence_model