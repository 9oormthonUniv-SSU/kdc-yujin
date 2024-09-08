from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from .forms import PostForm

def index(request):
   lottos = GuessNumbers.objects.all()
   return render(request, 'lotto/default.html', {'lottos': lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world! 🥸</h1>")

def post(request):
    if request.method == "POST":
        print(request.POST)
        print(request.method)

        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit = False) 
            print(type(lotto)) # <class 'lotto.models.GuessNumbers'>
            print(lotto)
            lotto.generate()
            return redirect('index')
        
    else:
        form = PostForm()
        return render(request, "lotto/form.html", {"form": form})
    
def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})
