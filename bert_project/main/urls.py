from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('bert_input/', views.bert_input, name='bert_input'),
]
