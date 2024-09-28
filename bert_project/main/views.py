from django.shortcuts import render
from django.utils import timezone # settings.py의 timezone을 따라감

def index(request):
    current_time = timezone.now()
    context = {'current_time':current_time}
    
    return render(request, 'main/index.html', context)
