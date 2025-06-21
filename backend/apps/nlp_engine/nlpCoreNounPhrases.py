import re
import spacy
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer, util

# Get text data
# text = open("data2.txt").read()
text = """Too Much Glucose in the Blood Diabetes means your blood glucose (often called blood sugar) is too high. Your blood always has some glucose in it because your body needs glucose for energy to keep you going. But too much glucose in the blood isn't good for your health. Glucose comes from the food you eat and is also made in your liver and muscles. Your blood carries the glucose to all of the cells in your body. Insulin is a chemical (a hormone) made by the pancreas. The pancreas releases insulin into the blood. Insulin helps the glucose from food get into your cells. If your body does not make enough insulin or if the insulin doesn't work the way it should, glucose can't get into your cells. It stays in your blood instead. Your blood glucose level then gets too high, causing pre-diabetes or diabetes. Types of Diabetes There are three main kinds of diabetes: type 1, type 2, and gestational diabetes. The result of type 1 and type 2 diabetes is the same: glucose builds up in the blood, while the cells are starved of energy. Over the years, high blood glucose damages nerves and blood vessels, oftentimes leading to complications such as heart disease, stroke, blindness, kidney disease, nerve problems, gum infections, and amputation. Type 1 Diabetes Type 1 diabetes, which used to be called called juvenile diabetes or insulin-dependent diabetes, develops most often in young people. However, type 1 diabetes can also develop in adults. With this form of diabetes, your body no longer makes insulin or doesnt make enough insulin because your immune system has attacked and destroyed the insulin-producing cells. About 5 to 10 percent of people with diabetes have type 1 diabetes. To survive, people with type 1 diabetes must have insulin delivered by injection or a pump. Learn more about type 1 diabetes here. Type 2 Diabetes Type 2 diabetes, which used to be called adult-onset diabetes or non insulin-dependent diabetes, is the most common form of diabetes. Although people can develop type 2 diabetes at any age -- even during childhood -- type 2 diabetes develops most often in middle-aged and older people. Type 2 diabetes usually begins with insulin resistancea condition that occurs when fat, muscle, and liver cells do not use insulin to carry glucose into the bodys cells to use for energy. As a result, the body needs more insulin to help glucose enter cells. At first, the pancreas keeps up with the added demand by making more insulin. Over time, the pancreas doesnt make enough insulin when blood sugar levels increase, such as after meals. If your pancreas can no longer make enough insulin, you will need to treat your type 2 diabetes. Learn more about type 2 diabetes here. Gestational Diabetes Some women develop gestational diabetes during the late stages of pregnancy. Gestational diabetes is caused by the hormones of pregnancy or a shortage of insulin. Although this form of diabetes usually goes away after the baby is born, a woman who has had it and her child are more likely to develop diabetes later in life. Prediabetes Prediabetes means your blood glucose levels are higher than normal but not high enough for a diagnosis of diabetes. People with prediabetes are at an increased risk for developing type 2 diabetes and for heart disease and stroke. The good news is that if you have prediabetes, you can reduce your risk of getting type 2 diabetes. With modest weight loss and moderate physical activity, you can delay or prevent type 2 diabetes.  Learn more about prediabetes here.  Signs of Diabetes Many people with diabetes experience one or more symptoms, including extreme thirst or hunger, a frequent need to urinate and/or fatigue. Some lose weight without trying. Additional signs include sores that heal slowly, dry, itchy skin, loss of feeling or tingling in the feet and blurry eyesight. Some people with diabetes, however, have no symptoms at all. How Many Have Diabetes? Nearly 29 million Americans age 20 or older (12.3 percent of all people in this age group) have diabetes, according to 2014 estimates from the Centers for Disease Control and Prevention (CDC). About 1.9 million people aged 20 years or older were newly diagnosed with diabetes in 2010 alone. People can get diabetes at any age, but the risk increases as we get older. In 2014, over 11 million older adults living in the U.S -- nearly 26 percent of people 65 or older -- had diabetes. See more statistics about diabetes from the  National Diabetes Statistics Report 2014. (Centers for Disease Control and Prevention.) If Diabetes is Not Managed Diabetes is a very serious disease. Over time, diabetes that is not well managed causes serious damage to the eyes, kidneys, nerves, heart, gums and teeth. If you have diabetes, you are more likely than people without diabetes to have heart disease or a stroke. People with diabetes also tend to develop heart disease or stroke at an earlier age than others. The best way to protect yourself from the serious complications of diabetes is to manage your blood glucose, blood pressure and cholesterol and to avoid smoking. It is not always easy, but people who make an ongoing effort to manage their diabetes can greatly improve their overall health.
"""

# Clean text preserving '.' and ','
cleanText = re.sub(r'[^\w\s\.,]', '', text)
cleanText = re.sub(r'\s+', ' ', cleanText).lower().strip()


# Extract noun phrases using spaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp(cleanText)
noun_phrases = [chunk.text for chunk in doc.noun_chunks]
# print("Noun Phrases: ", noun_phrases)


# Extract keyword score using keyBERT
# kw_model = KeyBERT()
# keywords = kw_model.extract_keywords(
#     cleanText,
#     keyphrase_ngram_range=(1,2),
#     stop_words='english'
# )
# print(keywords)


# Encode noun_phrases and the entire text and compare them to check relevancy of the keywords
model = SentenceTransformer('all-MiniLM-L6-v2')
doc_emb = model.encode(cleanText, convert_to_tensor=True)

results = []
for phrase in noun_phrases:
    ph_emb = model.encode(phrase, convert_to_tensor=True)
    score = util.cos_sim(doc_emb, ph_emb).item()
    results.append((phrase, score))

sorted_results = sorted(results, key=lambda x: x[1], reverse=True)


# Filter redundant data
seen = set()
unique_results = []
for phrase, score in sorted_results:
    key = phrase.lower().strip()
    if key not in seen:
        unique_results.append((phrase, score))
        seen.add(key)


print("\nTop Relevant Phrases:")
for phrase, score in unique_results:
    print(f"{phrase} --> {score}")