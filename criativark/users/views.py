from cmath import log
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import CreateAccForm, CreateProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashbord(request, username):
    user = User.objects.get(username=username)
    posts = user.post.all()
    context = {
        "user":user,
        "posts":posts,
        "has_post": posts.count() > 0
    }
    
    return render(request, "users/dashbord.html", context)


def creat_account(request):
    form = CreateAccForm()
    
    if request.method =="POST":
        form = CreateAccForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect ("first-login")
    
    context = {
        "form":form
    }
    return render(request, "users/create-account.html", context)



def create_profile(request):
    form = CreateProfile()
    
    if request.method == "POST":
        form = CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            
            return redirect("/")
            
    context ={
        "form":form
    }
    return render(request, "users/create-profile.html", context)



@login_required
def update_profile(request):
    profile = request.user.profile
    form = CreateProfile(instance=profile)
    
    if request.method == "POST":
        redirect_path = reverse("profile", args=[profile.slug])
        form = CreateProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_path)
            
    context = {
        "form":form
    }

    return render( request, "users/update-profile.html", context)



def profile(request, slug):
    try: 
        user_profile = Profile.objects.get(slug=slug)
    except:
        raise Http404
    
    user_profile_posts = user_profile.user.post.all()

    
    context ={
        "user_profile":user_profile,
        "user_profile_posts":user_profile_posts
    }
    
    return render(request, "users/profile.html", context)





def first_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect("create-profile")
        
        else:
           messages.info(request, "Password or Username is not correct")    

    context ={
        "message":messages
    }
    return render (request, "users/loguser.html", context)
           
         
         
           
               
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect("home")
        
        else:
           messages.info(request, "Password or Username is not correct")
    
    context ={
        "message":messages
    }
    return render (request, "users/loguser.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")





def delete_acc(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect("/")
    return render(request, "users/delete-user.html")