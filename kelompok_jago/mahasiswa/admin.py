from django.contrib import admin

# Register your models here.
from . models import Mhsw

class Tampil(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'kegiatan')
    list_display_links = (None)
    search_fields = ('nim','nama')

admin.site.register(Mhsw, Tampil)

