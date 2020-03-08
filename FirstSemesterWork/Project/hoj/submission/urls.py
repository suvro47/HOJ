from django.urls import path
from submission import views


urlpatterns = [
    path('status/', views.status, name='status'),
    path('my_status/', views.my_status, name='my_status'),
    path('single_status/<pid>/', views.single_status, name='single_status'),

]
