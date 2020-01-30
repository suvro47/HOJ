from django.shortcuts import render, redirect

from .models import Problem
from submission.models import Submission
from .forms import SubmitForm


#To view all problems
def problem_list(request):
    problems = Problem.objects.all().order_by('id')
    context = {'problems': problems}
    return render(request, 'problems.html', context)


def single_problem(request, pid):
    form = SubmitForm()
    problem = Problem.objects.get(id=pid)
    request.session['pid'] = pid
    context = {'problem': problem, 'form': form}
    return render(request, 'problem.html', context)