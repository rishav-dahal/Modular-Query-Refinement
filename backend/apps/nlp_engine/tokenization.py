import re
import spacy
# def tokenize_text(text):

#     """
#     Tokenizes the input text into words, removes punctuation, lowers case, removes numbers, whitespace, and stopwords,
#     and returns a list of words.
#     Args:
#         text (str): The input text to be tokenized.
#     Returns:
#         list: A list of words after tokenization, punctuation removal, lowercasing, number removal, whitespace stripping,
#               and stopwords removal.
#     """
#     # Lowercase
#     text = text.lower()
    
#     # Remove punctuation
#     text = re.sub(r'[^\w\s]', '', text)
    
#     # Remove numbers
#     text = re.sub(r'\d+', '', text)
    
#     # Strip whitespace
#     text = text.strip()
    
#     # Get stopwords
#     stop_words = set(nltk.corpus.stopwords.words('english'))
    
#     # Sentence tokenization
#     sentences = nltk.sent_tokenize(text)
    
#     # Word tokenization & stopwords removal
#     words = []
#     for sentence in sentences:
#         tokens = nltk.word_tokenize(sentence)
#         filtered_tokens = [word for word in tokens if word not in stop_words]
#         words.extend(filtered_tokens)
    
#     return words


def preprocess(text):
    """
    Preprocesses the input text by cleaning, tokenizing, lemmatizing, and filtering tokens.
    Args:
        text (str): The input text to be preprocessed.
    Returns:
        list: A list of lemmatized tokens after preprocessing.   
    """
    # 1. Clean text (preserve . and ,)
    cleanText = re.sub(r'[^\w\s\.,]', '', text)
    cleanText = re.sub(r'\s+', ' ', cleanText).lower().strip()
    cleanText = re.sub(r'\d+', '', cleanText)

    nlp = spacy.load("en_core_web_sm")
    # 2. Tokenize and Lemmatize
    doc = nlp(cleanText)

     # 3. Filter tokens: lemmatize, remove stopwords/punctuation, keep only NOUN and ADJ
    lemmatized_tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and token.is_alpha
        and token.pos_ in ["NOUN", "ADJ", "VERB"]
    ]

    return lemmatized_tokens

