# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet

# # Helper function to convert nltk POS tag to wordnet POS tag (needed for better lemmatization)
# def get_wordnet_pos(treebank_tag):
    
#     """
#     Converts treebank POS tags to wordnet POS tags.
#     Args:
#         treebank_tag (str): The POS tag in treebank format.
#     Returns:
#         str: The corresponding wordnet POS tag.
#     """

#     if treebank_tag.startswith('J'):
#         return wordnet.ADJ
#     elif treebank_tag.startswith('V'):
#         return wordnet.VERB
#     elif treebank_tag.startswith('N'):
#         return wordnet.NOUN
#     elif treebank_tag.startswith('R'):
#         return wordnet.ADV
#     else:
#         return wordnet.NOUN  # default to noun if unknown

# # Get POS tags for words
# def lemmatize_word(words):

#     """
#     Lemmatizes a list of words using NLTK's WordNetLemmatizer.
#     Args:
#         words (list): A list of words to be lemmatized.
#     Returns:
#         list: A list of lemmatized words.
#     """
#     lemmatizer = WordNetLemmatizer()
#     pos_tags = nltk.pos_tag(words)

#     lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]
#     return lemmatized_words
