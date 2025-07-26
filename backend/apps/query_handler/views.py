# from .serializers import QuerySerializer
import json
from apps.nlp_engine.tokenization import preprocess
from apps.nlp_engine.utils_data import load_models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from sentence_transformers import SentenceTransformer


@api_view(['POST'])
def submit_query(request):
    try:
        query = request.data.get("query")
        flag = request.data.get("flag")
        lda_model, lda_dictionary , lsi_model , lsi_dictionary , optimal_lda_model, optimal_lda_dictionary , lsi_tfidf_model , bert_model, cluster_keywords, sentence_model = load_models()

        print(f"Received query: {query} with flag: {flag}")
        if not query or not flag:
            return Response({"error":"Missing query or flag"}, status=status.HTTP_400_BAD_REQUEST)

        if flag == "LDA":
            preprocessed_query = preprocess(query,flag="LDA")
            bow_query = lda_dictionary.doc2bow(preprocessed_query)
            topic_distribution = lda_model.get_document_topics(bow_query)
            top_topic = max(topic_distribution, key=lambda x: x[1])[0]
            keywords = lda_model.show_topic(top_topic, topn=10)
            return Response({"data":keywords}, status=status.HTTP_200_OK)

        elif flag == "LSA":
            preprocessed_query = preprocess(query,flag="NONE")
            bow_query = lsi_dictionary.doc2bow(preprocessed_query)
            tfidf_query = lsi_tfidf_model[bow_query]
            topic_distribution = lsi_model[tfidf_query]

            if topic_distribution:
                top_topic_id = max(topic_distribution, key=lambda x: abs(x[1]))[0] # Use absolute value for LSI scores

                all_topics_terms = lsi_model.show_topics(num_topics=-1, formatted=False)
                keywords = None
                for topic_id, terms in all_topics_terms:
                    if topic_id == top_topic_id:
                        keywords = terms
                        break

                if keywords:
                    # Sort keywords by absolute score and take the top N
                    keywords = sorted(keywords, key=lambda x: abs(x[1]), reverse=True)[:10] # Top 10 keywords
                    return Response(keywords, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "No keywords found for the dominant topic."}, status=status.HTTP_404_NOT_FOUND)

            else:
                return Response({"error": "No topics found for the query."}, status=status.HTTP_404_NOT_FOUND)

        elif flag == "LDA_VERB":
            preprocessed_query = preprocess(query,flag="NONE")
            bow_query = optimal_lda_dictionary.doc2bow(preprocessed_query)
            topic_distribution = optimal_lda_model.get_document_topics(bow_query)
            top_topic = max(topic_distribution, key=lambda x: x[1])[0]
            keywords = optimal_lda_model.show_topic(top_topic, topn=10)
            return Response(keywords, status=status.HTTP_200_OK)
        
        elif flag == "BERT":
            query_embedding = sentence_model.encode([query])
            cluster_id = bert_model.predict(query_embedding)[0]
            keywords =cluster_keywords.get(str(cluster_id))

            return Response(keywords, status=status.HTTP_200_OK)
        else:
            return Response({"error": f"Unsupported flag: {flag}"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(f"Error processing query: {e}")
        return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)