from django.shortcuts import render, redirect

# Create your views here.
from app.forms import BlogForm
from app.models import Blog


def start_page(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'start.html', context)


def blog_page(request, param):
    if request.method == "POST":
        post = Blog.objects.get(pk=param)
        post.likes += 1
        post.save()
    blog = Blog.objects.get(pk=param)
    context = {"blog": blog}
    return render(request, 'blog.html', context)


def create_blog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author_name']
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            Blog.objects.create(author=author, title=title, text=text, likes=0)
            return redirect('start')
        else:
            context = {"form": form}
            return render(request, 'create_blog.html', context)
    else:
        context = {"form": form}
        return render(request, 'create_blog.html', context)