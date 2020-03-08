from django.urls import path
from contest import views as views

urlpatterns = [
    path('contests/', views.contest_list, name='contests'),
    path('contest/<cid>/', views.contest, name='contest'),
    path('contest_end/<cid>/', views.contest_end, name='contest_end'),
    path('contest/<cid>/problem/<pid>/', views.cont_problem, name='cont_problem'),
    path('contest/<cid>/standings/', views.contest_standings, name='contest_standings'), 
]


