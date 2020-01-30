from django.shortcuts import render, redirect
from problem.models import Problem
from submission.models import Submission
from .forms import SubmitForm
from judge_dir.judge import judging


#To view all problems
def problem_list(request):
    problems = Problem.objects.all().order_by('id')
    context = {'problems': problems}
    return render(request, 'problems.html', context)


def single_problem(request, pid):
    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            code = form.save(commit=False)  # variable name need to change
            code.user_id = request.user
            problem = Problem.objects.get(id=pid)
            problem.no_of_submissions += 1
            code.problem_id = problem
            code.save()  # save the model before judging with default values
            time = problem.time_limit
            code.verdict, code.time = judging(problem.input_file.path, problem.output_file.path, code.code.path, code.language, time, problem.memory_limit)
            if code.verdict == 1:
                problem.no_of_accepted += 1
            # final save after judging
            code.save()
            problem.save()
            return redirect('submission')  # after submit redirect to submission page
    else:
        form = SubmitForm()
        problem = Problem.objects.get(id=pid)
        request.session['pid'] = pid
        context = {'problem': problem, 'form': form}
        return render(request, 'problem.html', context)


#To view all submissions, function name need to change
def submit_code(request):
    submission = Submission.objects.all().order_by('-id') #descending order
    context = {'submission': submission}
    return render(request, 'submit.html', context)





