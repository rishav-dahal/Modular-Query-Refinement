# import re
# import spacy
# from keybert import KeyBERT
# from sentence_transformers import SentenceTransformer, util

# # Get text data
# # text = open("data2.txt").read()
# text = """Built a responsive web interface using Nuxt.js framework - Leveraged server-side rendering for better performance and SEO
# N"""

# # Clean text preserving '.' and ','
# cleanText = re.sub(r'[^\w\s\.,]', '', text)
# cleanText = re.sub(r'\s+', ' ', cleanText).lower().strip()


# # Extract noun phrases using spaCy
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(cleanText)
# noun_phrases = [chunk.text for chunk in doc.noun_chunks]
# # print("Noun Phrases: ", noun_phrases)


# # Extract keyword score using keyBERT
# # kw_model = KeyBERT()
# # keywords = kw_model.extract_keywords(
# #     cleanText,
# #     keyphrase_ngram_range=(1,2),
# #     stop_words='english'
# # )
# # print(keywords)


# # Encode noun_phrases and the entire text and compare them to check relevancy of the keywords
# model = SentenceTransformer('all-MiniLM-L6-v2')
# doc_emb = model.encode(cleanText, convert_to_tensor=True)

# results = []
# for phrase in noun_phrases:
#     ph_emb = model.encode(phrase, convert_to_tensor=True)
#     score = util.cos_sim(doc_emb, ph_emb).item()
#     results.append((phrase, score))

# sorted_results = sorted(results, key=lambda x: x[1], reverse=True)


# # Filter redundant data
# seen = set()
# unique_results = []
# for phrase, score in sorted_results:
#     key = phrase.lower().strip()
#     if key not in seen:
#         unique_results.append((phrase, score))
#         seen.add(key)


# print("\nTop Relevant Phrases:")
# for phrase, score in unique_results:
#     print(f"{phrase} --> {score}")