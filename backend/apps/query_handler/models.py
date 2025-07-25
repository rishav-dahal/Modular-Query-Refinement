from django.db import models

class Query(models.Model):

    """
    Model to store user queries and their refined versions.
    """

    id = models.AutoField(primary_key=True)
    raw_query = models.TextField()
    keywords = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query {self.id}: {self.raw_query[:20]}..."
