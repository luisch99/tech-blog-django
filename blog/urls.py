from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('crear/', views.crear_post, name='crear_post'),
    path('registro/', views.registro, name='registro'),
    path('editar/<int:post_id>/', views.editar_post, name='editar_post'),
]