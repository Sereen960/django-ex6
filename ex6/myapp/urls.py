from django.urls import path
from .views import create1, read, update, delete

urlpatterns = [
    path('createtab/', create1, name='createtab'),
    path('readtab/', read, name='readtab'),
    path('<int:pk>/updatetab/', update, name='updatetab'),
    path('<int:pk>/deletetab/', delete, name='deletetab'),  # Ensure this line captures pk correctly
]
