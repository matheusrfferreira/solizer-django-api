from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.UserView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('users/<int:user_id>/', views.EditUserView.as_view()),
    path('users/clients/', views.ClientView.as_view()),
    path('users/integrators/', views.IntegratorView.as_view()),
]
