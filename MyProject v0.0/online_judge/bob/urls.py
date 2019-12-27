from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-list/', views.user_list, name='user-list'),
    path('single-user/<user_id>/', views.single_user, name='single-user'),
]
