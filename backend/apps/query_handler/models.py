from django.db import models

class Query(models.Model):

    """
    Model to store user queries and their refined versions.
    """

    id = models.AutoField(primary_key=True)
    raw_query = models.TextField()
    refined_query = models.TextField()
    user_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query {self.id} by User {self.user_id}: {self.raw_query[:20]}..."
