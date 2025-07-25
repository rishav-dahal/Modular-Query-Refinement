# import re
# import spacy
# import gensim
# from gensim import corpora, models
# from gensim.models import CoherenceModel

# def preprocess(text):
#     # ...existing code...
#     cleanText = re.sub(r'[^\w\s\.,]', '', text)
#     cleanText = re.sub(r'\s+', ' ', cleanText).lower().strip()
#     cleanText = re.sub(r'\d+', '', cleanText)
#     doc = spacy.load("en_core_web_sm")(cleanText)
#     lemmatized_tokens = [
#         token.lemma_.lower()
#         for token in doc
#         if not token.is_stop
#         and not token.is_punct
#         and token.is_alpha
#         and token.pos_ in ["NOUN", "ADJ"]
#     ]
#     return lemmatized_tokens

# def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=1):
#     coherence_values = []
#     model_list = []
#     for num_topics in range(start, limit, step):
#         model = models.LdaModel(corpus=corpus,
#                                 id2word=dictionary,
#                                 num_topics=num_topics,
#                                 random_state=42,
#                                 passes=10)
#         model_list.append(model)
#         coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
#         coherence_values.append(coherencemodel.get_coherence())
#     return model_list, coherence_values

# if __name__ == "__main__":
#     # Get text data
#     text = """Built a responsive web interface using Nuxt.js framework - Leveraged server-side rendering for better performance and SEO
# """
#     tokens = preprocess(text)
#     texts = [tokens]
#     dictionary = corpora.Dictionary(texts)
#     corpus = [dictionary.doc2bow(text) for text in texts]
#     start, limit, step = 2, 15, 1
#     model_list, coherence_values = compute_coherence_values(dictionary, corpus, texts, limit, start, step)
#     best_index = coherence_values.index(max(coherence_values))
#     optimal_model = model_list[best_index]
#     optimal_num_topics = start + best_index
#     print(f"\n Best Number of Topics: {optimal_num_topics}")
#     top_keywords = optimal_model.show_topic(0, topn=10)
#     print("\n Top Keywords from Dominant Topic:")
#     for word, prob in top_keywords:
#         print(f"{word} ({prob:.4f})")