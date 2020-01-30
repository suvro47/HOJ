from django.shortcuts import render
from problem.models import Problem


#To view all problems
def problem_list(request):
    problems = Problem.objects.all().order_by('id')
    context = {'problems': problems}
    return render(request, 'problems.html', context)

def single_problem( request , pid ):
    problem = Problem.objects.get(pk=pid)
    return render(request, 'problem.html', {'problem': problem})

