from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("create-account", views.creat_account, name="create-account"),
    path("create-profile/", views.create_profile, name="create-profile"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("update-profile/", views.update_profile, name="update-profile"),
    path("profile/<slug:slug>", views.profile, name="profile"),
    path("dashbord/<str:username>", views.dashbord, name="dashbord"),
    path("first-login", views.first_login, name="first-login"),
    path("delete-acc", views.delete_acc, name="delete-acc"),
    

    

    path("reset_password", auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name="reset_password"),
    path("reset_password_done", auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="users/reset_password_form.html"), name="password_reset_confirm"),
    path("reset_complete", auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"), name="password_reset_complete")
]
