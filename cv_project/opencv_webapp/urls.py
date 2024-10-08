from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'opencv_webapp'

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name='detect_face'),
]

# settings.py에 정의해둔 경로를 사용
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)