from rest_framework import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuerySerializer

@api_view(['POST'])
def submit_query(request):
    
    """
    API endpoint to submit a user query and receive a refined version.
    """

    serializer = QuerySerializer(data=request.data)
    if serializer.is_valid():
        query_instance = serializer.save()
        return Response({'refined_query': query_instance.refined_query , 'raw_query': query_instance.raw_query}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

