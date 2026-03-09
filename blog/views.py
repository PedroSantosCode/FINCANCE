from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    related_posts = BlogPost.objects.filter(published=True).exclude(pk=post.pk)[:3]
    return render(request, 'blog/blog_detail.html', {'post': post, 'related_posts': related_posts})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Post criado com sucesso!')
            return redirect('blog_list')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao criar post. Verifique os campos.')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_create.html', {'form': form})


@login_required
def blog_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Post atualizado com sucesso!')
            return redirect('blog_detail', slug=post.slug)
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao atualizar post. Verifique os campos.')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blog_edit.html', {'form': form, 'post': post})
