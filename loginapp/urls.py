from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    # user submit email
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name='reset_password'),

    # email sent message 
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name='password_reset_done'),

    # email with link and reset instruction 
    # this encodes user id in a base of 64,makes sure that email is send to a specified user
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name='password_reset_confirm'),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_compete.html"),
         name='password_reset_complete'),

    
]