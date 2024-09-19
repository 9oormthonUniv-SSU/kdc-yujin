from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'opencv_webapp'

urlpatterns = [
    path('', views.first_view, name='first_view'),
]