from django.shortcuts import render, redirect
from problem.models import Problem
from user.models import CustomUser
from .forms import SubmitForm
from submission.models import Submission
from Judge_dir.judge import judging
from django.contrib.auth.models import User
from django.db.models import Q  # perform searching
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# pagination ref : https://www.youtube.com/watch?v=q-Pw7Le30qQ

#To view all problems
def problem_list(request):
    problems = Problem.objects.all().order_by('id')
    # make searching 
    query = request.GET.get("q")
    if query:
       problems = problems.filter(
           Q(tags__icontains=query) |
           Q(difficulty__icontains=query)
           )  

    context = {'problems': problems}
    return render(request, 'problems.html', context)

def single_problem(request, pid):
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            code = form.save(commit=False)  # variable name need to change
            code.user_id = request.user
            problem = Problem.objects.get(id=pid)
            # user submission have to increase
            problem.no_of_submissions += 1
            code.problem_id = problem
            code.save()  # save the model before judging with default values
            if code.language == 'Python':  # Time limit for different language
                time = problem.time_limit[1]
            else:
                time = problem.time_limit[0]
            
            code.verdict, code.time = judging(problem.input_file.path, problem.output_file.path, code.code.path, code.language, time, problem.memory_limit)
            current_user = CustomUser.objects.get(id=request.user.id)
            current_user.problem_tried += 1
            print(current_user.problem_tried)
            if code.verdict == 1:
               current_user.problem_solved += 1
               problem.no_of_accepted += 1
            code.save()
            problem.save()
            current_user.save()
            return redirect('single_status' , pid )  # after submit redirect to user_submission page
    else:
        form = SubmitForm()
        problem = Problem.objects.get(id=pid)
        request.session['pid'] = pid
        context = {'problem': problem, 'form': form}
        return render(request, 'problem.html', context)


