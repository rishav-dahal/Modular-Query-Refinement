from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .serializers import QuerySerializer
from apps.nlp_engine.tokenization import preprocess
import json
from apps.nlp_engine.utils_data import load_models
@api_view(['POST'])
def submit_query(request):
    try:
        data = json.loads(request.body)
        query = data.get("query")
        flag = data.get("flag")

        if not query or not flag:
            return Response({"error":"Missing query or flag"}, status=status.HTTP_400_BAD_REQUEST)

        preprocessed_query = preprocess(query)

        if flag == "LDA":
            optimal_model, dictionary = load_models()
            bow_query = dictionary.doc2bow(preprocessed_query)
            topic_distribution = optimal_model.get_document_topics(bow_query)
            top_topic = max(topic_distribution, key=lambda x: x[1])[0]
            keywords = optimal_model.show_topic(top_topic, topn=10)
            return Response(keywords, status=status.HTTP_200_OK)

        # elif flag == "LSI":
        #     result = run_sbert(query)
        # elif flag == "lda":
        #     result = run_lda(query)
        # else:
        #     return Response({"error": f"Unsupported flag: {flag}"}, status=status.HTTP_400_BAD_REQUEST)

        

    except Exception as e:
        print(f"Error processing query: {e}")
        return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"error": "Only POST method is allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)