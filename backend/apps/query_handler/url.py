from django.urls import path
from .views import submit_query

urlpatterns = [
    path('submit/', submit_query, name='submit_query'),
]