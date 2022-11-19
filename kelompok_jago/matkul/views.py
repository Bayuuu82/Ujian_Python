from django.shortcuts import render

# Create your views here.
from . models import Post

def index(request):
    postingan = Post.objects.all()
    
    context = {'Tampungpostingan': postingan,}
    return render(request, 'matkul/index.html', context)