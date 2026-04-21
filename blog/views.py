from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Post, Categoria
from .forms import PostForm, RegistroUsuarioForm
from django.shortcuts import get_object_or_404

def bloquear_admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        logout(request)
        messages.error(request, "La cuenta admin solo puede usarse en /admin/.")
        return True
    return False


def home(request):
    if bloquear_admin(request):
        return redirect('login')
    return render(request, 'blog/home.html')


def lista_posts(request):
    if bloquear_admin(request):
        return redirect('login')

    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')

    posts = Post.objects.filter(estado='publicado')

    if query:
        posts = posts.filter(titulo__icontains=query)

    if categoria:
        posts = posts.filter(categoria__id=categoria)

    posts = posts.order_by('-fecha_publicacion')
    categorias = Categoria.objects.all()

    return render(request, 'blog/list.html', {
        'posts': posts,
        'query': query,
        'categorias': categorias,
        'categoria_seleccionada': categoria
    })


@login_required
def crear_post(request):
    if bloquear_admin(request):
        return redirect('login')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()

    return render(request, 'blog/form.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'blog/register.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                messages.error(request, "Este usuario solo puede acceder desde el panel admin.")
                return redirect('login')

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'blog/login.html')


@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Solo el autor puede editar
    if request.user != post.autor:
        return redirect('lista_posts')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/form.html', {'form': form})