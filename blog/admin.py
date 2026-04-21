from django.contrib import admin
from .models import Post, Categoria, Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'estado', 'fecha_publicacion')
    list_filter = ('estado', 'categoria')
    search_fields = ('titulo', 'contenido')
    ordering = ('-fecha_publicacion',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'post', 'fecha_creacion')
    search_fields = ('autor', 'contenido')
    list_filter = ('fecha_creacion',)