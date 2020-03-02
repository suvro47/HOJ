from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def basic(request):
    return render(request, 'resources/basic.html')

def programming_language(request):
    return render(request, 'resources/programming_language.html')

def sort_search(request):
    return render(request, 'resources/sort_search.html')

def ds(request):
    return render(request, 'resources/ds.html')

def mnt(request):
    return render(request,'resources/mnt.html')

def graph_theory(request):
    return render(request,'resources/graph_theory.html')

def recursion(request):
    return render(request,'resources/recursion.html')

def DP(request):
    return render(request,'resources/DP.html')
