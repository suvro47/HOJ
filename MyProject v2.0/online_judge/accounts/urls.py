from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),  Django has it's own login/logout views
    # path('logout/', views.logout, name='logout'),  you don't need to define it and reference it to template
]
