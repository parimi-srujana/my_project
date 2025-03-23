from django.urls import path
from .views import insert_rows, person_list
urlpatterns = [
    path('insert/', insert_rows, name='insert'),
    path('', person_list, name='person_list'),
]