from django.shortcuts import render
from django.forms import ModelForm
from .models import Files


# Create your views here.
def file_upload(request):
    queryset = Files.objects.all()
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        file_list = []
        for file in files:
            new_file = Files(
                file=file
            )
            file_list.append(new_file.file.url)
            new_file.save()
        return render(request, 'index.html', {'file_urls': file_list,'objects': queryset})
    else:
        return render(request, 'index.html',{'objects': queryset})
