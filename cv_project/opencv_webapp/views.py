from django.shortcuts import render

def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})