from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("posts/", views.posts, name="posts"),
    path("add-post/", views.new_post, name="add-post"),
    path("update-post/<slug:slug>", views.update_post, name="update-post"),
    path("delete/<slug:slug>", views.delete_post, name="delete-post"),
    path("detail/<slug:slug>",  views.detail, name="detail")
]
