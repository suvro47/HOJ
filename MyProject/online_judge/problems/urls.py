from django.urls import path
from .import views


urlpatterns = [
    path('problem-list/', views.problem_list, name='problem-list'),
    path('single-problem/<problem_id>/', views.single_problem, name='single-problem'),
]
