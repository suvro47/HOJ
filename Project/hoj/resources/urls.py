from django.urls import path
from resources import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('basic/', views.basic, name='basic'),
    path('pro_lang/', views.programming_language, name='pro_lang'),
    path('sort_search/', views.sort_search, name='sort_search'),
    path('ds/', views.ds, name='ds'),
    path('mnt/',views.mnt, name='mnt'),
    path('graph_theory/',views.graph_theory, name='graph_theory'),
    path('recursion/',views.recursion, name='recursion'),
    path('dp/',views.DP, name='DP'),

]
