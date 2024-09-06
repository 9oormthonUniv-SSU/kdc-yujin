from django.shortcuts import render
from django.http import HttpResponse
from lotto.models import GuessNumbers

def index(request):
 lottos = GuessNumbers.objects.all()
 return render(request, 'lotto/default.html', {'lottos': lottos})

def hello(request):
 return HttpResponse("<h1 style='color:red;'>Hello, world! 🥸</h1>")
