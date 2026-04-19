from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    query = request.GET.get('q', '')
    
    if query:
        posts = Post.objects.filter(
            titulo__icontains=query,
            estado='publicado'
        ).order_by('-fecha_publicacion')
    else:
        posts = Post.objects.filter(
            estado='publicado'
        ).order_by('-fecha_publicacion')

    return render(request, 'blog/inicio.html', {
        'posts': posts,
        'query': query
    })

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('inicio')
    else:
        form = PostForm()

    return render(request, 'blog/crear_post.html', {'form': form})