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


def preprocess(text,flag):
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
    lemmatized_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct or not token.is_alpha:
            continue

        if flag == "LDA":
            if token.pos_ in ["NOUN", "ADJ"]:
                lemmatized_tokens.append(token.lemma_.lower())
        elif flag == "NONE":
            if token.pos_ in ["NOUN", "ADJ", "VERB"]:
                lemmatized_tokens.append(token.lemma_.lower())
        else:
            # Default fallback: keep all content words
            if token.pos_ in ["NOUN", "ADJ", "VERB"]:
                lemmatized_tokens.append(token.lemma_.lower())

    return lemmatized_tokens

