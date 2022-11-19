from django.shortcuts import render

# Create your views here.
from . forms import Mahasiswa
from . models import Mhsw

def index(request):
    list_mhs = Mahasiswa()

    context = {
        'Listmhs': list_mhs,
    }
    
    if request.method == 'POST':
        Mhsw.objects.create(
            nim = request.POST.get('nim'),
            nama = request.POST.get('nama'),
            kegiatan = request.POST.get('kegiatan'),
    )
    return render(request, 'mahasiswa/index.html', context)