from django.db import models

# Create your models here.
class Post(models.Model):
    nama_matkul = models.CharField(max_length=255)
    dosen = models.CharField(max_length=255)
    materi = models.TextField()

    def __str__(self):
        return self.nama_matkul
