# urls.py

from django.urls import path
from .views import MyDataAPIView

urlpatterns = [
    path('api/mydata/', MyDataAPIView.as_view(), name='mydata-list'),
]
    # Add more URL patterns as needed]
