from rest_framework import serializers
from .models import Query
from apps.nlp_engine.tokenization import tokenize_text

class QuerySerializer(serializers.ModelSerializer):

    """
    Serializer for handling user queries and their refined versions.
    """
    
    refined_query = serializers.CharField(read_only=True)

    class Meta:
        model = Query
        fields = ['id', 'raw_query', 'refined_query', 'timestamp']

    def create(self, validated_data):
        raw_query = validated_data.get('raw_query')

        refined_query = tokenize_text(raw_query) # pipeline_process(raw_query)

        return Query.objects.create(
            raw_query=raw_query,
            refined_query=refined_query,
        )
