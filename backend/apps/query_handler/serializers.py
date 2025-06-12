from rest_framework import serializers
from .models import Query

class QuerySerializer(serializers.ModelSerializer):

    """
    Serializer for handling user queries and their refined versions.
    """
    
    refined_query = serializers.CharField(read_only=True)

    class Meta:
        model = Query
        fields = ['id', 'raw_query', 'refined_query', 'user_id', 'timestamp']

    def create(self, validated_data):
        raw_query = validated_data.get('raw_query')
        user_id = validated_data.get('user_id')

        refined_query = None # pipeline_process(raw_query)

        return Query.objects.create(
            raw_query=raw_query,
            refined_query=refined_query,
            user_id=user_id
        )
