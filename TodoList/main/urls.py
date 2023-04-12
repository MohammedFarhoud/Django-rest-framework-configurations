from django.urls import path
from .views import goHome, getAlltodos
urlpatterns = [
    path('', goHome, name='home'),
    path('todos/', getAlltodos, name='todos'),
]