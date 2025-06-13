import re
import nltk

def tokenize_text(text):

    """
    Tokenizes the input text into words, removes punctuation, lowers case, removes numbers, whitespace, and stopwords,
    and returns a list of words.
    Args:
        text (str): The input text to be tokenized.
    Returns:
        list: A list of words after tokenization, punctuation removal, lowercasing, number removal, whitespace stripping,
              and stopwords removal.
    """
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Strip whitespace
    text = text.strip()
    
    # Get stopwords
    stop_words = set(nltk.corpus.stopwords.words('english'))
    
    # Sentence tokenization
    sentences = nltk.sent_tokenize(text)
    
    # Word tokenization & stopwords removal
    words = []
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        filtered_tokens = [word for word in tokens if word not in stop_words]
        words.extend(filtered_tokens)
    
    return words


