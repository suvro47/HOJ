from django.urls import path
from problem import views


urlpatterns = [
    path('problems/', views.problem_list, name='problems'),
    path('problem/<pid>/', views.single_problem, name='problem'),
]
