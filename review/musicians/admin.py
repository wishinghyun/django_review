from django.contrib import admin
from .models import Musician, Album, Song

# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('musician', 'album_name', 'created_at')

class SongAdmin(admin.ModelAdmin):
    list_display = ('album', 'title')

admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)