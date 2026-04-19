from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'estado', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido', 'categoria')
    list_filter = ('estado', 'categoria', 'fecha_publicacion')