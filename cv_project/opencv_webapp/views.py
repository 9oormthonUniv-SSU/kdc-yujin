from django.shortcuts import render, redirect
from .forms import SimpleUploadForm
from django.core.files.storage import FileSystemStorage

def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})

def simple_upload(request):
    if request.method == 'POST':
       form = SimpleUploadForm(request.POST, request.FILES)
       
       if form.is_valid():
          myfile = request.FILES['image']
          fs = FileSystemStorage()
          filename = fs.save(myfile.name, myfile)
          uploaded_file_url = fs.url(filename) # '/media/*.jpg'
          
          context = {'form': form, 'uploaded_file_url': uploaded_file_url}
          return render(request, 'opencv_webapp/simple_upload.html', context)
       
    else:
       form = SimpleUploadForm()
       context = {'form': form}
       return render(request, 'opencv_webapp/simple_upload.html', context)
