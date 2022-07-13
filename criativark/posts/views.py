from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Post
from .forms import NewPostForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by("-date")[:3]
    context = {
        "posts":posts
    }
    return render(request, "posts/index.html", context)


def about(request):
    return render(request, "posts/about.html")

def posts(request):
    posts = Post.objects.all().order_by("-date")
    search_term = request.GET.get("search_term")
    if search_term !="" and search_term is not None:
        posts = posts.filter(title__icontains=search_term)
    paginate =  Paginator(posts, 6)
    page_num = request.GET.get("page")
    page_posts = paginate.get_page(page_num)
    
    context = {
        "posts":page_posts,
        
    }
    return render(request, "posts/posts.html", context)



def detail(request, slug):
    form = CommentForm()
    try:
        post = Post.objects.get(slug=slug)
        
    except:
        raise Http404()
    post_tags  = post.tag.all()
    related_posts = Post.objects.filter(tag__in=post_tags).exclude(slug=slug)
    comments = post.comments_set.all().order_by("-id")
    
    if request.method == "POST":
        redirect = reverse("detail", args=[post.slug])
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.save()
            return HttpResponseRedirect(redirect)
    context ={
        "post":post,
        "post_tags":post_tags,
        "related_posts":related_posts,
        "comments":comments,
        "has_comment":comments.count() > 0,
        "form":form
    }
    return render(request, "posts/detail.html", context)

@login_required
def new_post(request):
    form = NewPostForm()
    if request.method == "POST":
        user = request.user
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect("posts")
            
    
    context ={
        "form":form
    }
    return render(request, "posts/newpost.html", context)

@login_required
def update_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except:
        raise Http404
    
    form = NewPostForm(instance=post)
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect("posts")
    context ={
        "form":form
    }
    return render(request, "posts/update.html", context)

@login_required
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        redirect = reverse("dashbord", args=[post.author])
        post.delete()
        return HttpResponseRedirect(redirect)
    
    context = {
        "post":post
    }

    return render(request, "posts/delete.html", context)

