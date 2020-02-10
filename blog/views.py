from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Tag
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import TagForm
from .forms import AddTagForm
from .forms import FilterForm
from django.shortcuts import redirect

def post_list(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            posts = Post.objects.filter(tag__tag=form.cleaned_data['fil'])
            return render(request, 'blog/post_list.html', {'posts': posts ,'form':form})
    else:
        form = FilterForm()
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts ,'form':form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tag = Tag.objects.filter(posts__id=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'tag':tag})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def tag_new(request):
    form = TagForm()
    return render(request, 'blog/tag_add.html', {'form': form})

def tag_new(request):
    if request.method == "POST":
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        form = TagForm(request.POST)
        if form.is_valid():
            newTag = form.cleaned_data['tag']
            tag = Tag(tag=newTag)
            tag.save()
            return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = TagForm()
    return render(request, 'blog/tag_add.html', {'form': form})


def add_tag_post(request ,pk):
    if request.method == "POST":
        form = AddTagForm(request.POST)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            id = form.cleaned_data['tag']
            id = int(id[0])
            newTag = Tag.objects.get(pk=id)
            newTag.posts.add(post)
            newTag.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = AddTagForm()
    return render(request, 'blog/post_add_tag.html', {'form': form})



