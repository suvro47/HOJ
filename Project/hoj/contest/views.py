from django.shortcuts import render, redirect
from contest.models import Contest
from problem.models import Problem
from user.models import CustomUser
from .forms import SubmitForm
from submission.models import Submission
from Judge_dir.judge import judging
from django.contrib.auth.models import User
from django.utils import timezone


#To view all Contests
def contest_list(request):
    contests = Contest.objects.all().order_by('id')
    context = {'contests': contests}
    return render(request, 'contest/contests.html', context)

#To view problems of a specific contest
def contest(request,cid):
    contest = Contest.objects.get(id=cid)
    
    # lame kaj korlam :(  Iterate kore korte hbe ... 
    if contest.no_of_problem >= 1:
        prob1 = Problem.objects.get(id=contest.problem_list[0])
    if contest.no_of_problem >= 2: 
        prob2 = Problem.objects.get(id=contest.problem_list[1])
    if contest.no_of_problem >= 3: 
        prob3 = Problem.objects.get(id=contest.problem_list[2])
    if contest.no_of_problem >= 4: 
        prob4 = Problem.objects.get(id=contest.problem_list[3])
    if contest.no_of_problem >= 5: 
        prob5 = Problem.objects.get(id=contest.problem_list[4])
    if contest.no_of_problem >= 6: 
        prob6 = Problem.objects.get(id=contest.problem_list[5])
    if contest.no_of_problem >= 7: 
        prob7 = Problem.objects.get(id=contest.problem_list[6])
    
    if timezone.now() > contest.end_time :
        status = "Finished !!"
    else :
        status = "Running...."  
    
    if contest.no_of_problem == 1:
        context = {'contest': contest, 'prob1': prob1 }
    elif contest.no_of_problem == 2:
        context = {'contest': contest, 'prob1': prob1 , 'prob2': prob2 }    
    elif contest.no_of_problem == 3:
        context = {'contest': contest, 'prob1': prob1 , 'prob2': prob2, 'prob3': prob3 }        
    elif contest.no_of_problem == 4:
        context = {'contest': contest, 'prob1': prob1 , 'prob2': prob2, 'prob3': prob3, 'prob4': prob4 ,  'status': status }
    elif contest.no_of_problem == 5:
        context = {'contest': contest, 'prob1': prob1 , 'prob2': prob2, 'prob3': prob3, 'prob4': prob4 , 'prob5': prob5 }
    elif contest.no_of_problem == 6:
        context = {'contest': contest, 'prob1': prob1 , 'prob2': prob2, 'prob3': prob3, 'prob4': prob4 , 'prob5': prob5 , 'prob6': prob6 }
    elif contest.no_of_problem == 7:
        context = {'contest': contest, 'prob1': prob1 , 'prob2': prob2, 'prob3': prob3, 'prob4': prob4 , 'prob5': prob5 , 'prob6': prob6 , 'prob7':prob7 }

    return render(request, 'contest/contest.html', context)

# Contest ended :(   
def contest_end(request,cid):
    contest = Contest.objects.get(id=cid)
    context = {'contest': contest}
    return render(request, 'contest/contest_end.html', context) 
    
#To View contest Problem
def cont_problem(request, pid, cid):
    if request.method == 'POST':
        contest = Contest.objects.get(id=cid)
        if timezone.now() > contest.end_time :
            return redirect('contest_end' , contest.id )  # show contest end message    
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            code = form.save(commit=False)  # variable name need to change
            code.user_id = request.user
            
            # Current Problem 
            problem = Problem.objects.get(id=pid)
            problem.no_of_submissions += 1

            # current user
            current_user = CustomUser.objects.get(id=request.user.id)
            current_user.problem_tried += 1

            code.problem_id = problem
            code.save()  # save the model before judging with default values
            if code.language == 'Python':  # Time limit for different language
                time = problem.time_limit[1]
            else:
                time = problem.time_limit[0]
  
            code.verdict, code.time = judging(problem.input_file.path, problem.output_file.path, code.code.path, code.language, time, problem.memory_limit)
            
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
        contest = Contest.objects.get(id=cid)
        request.session['pid'] = pid
        context = {'problem': problem, 'contest': contest, 'form': form}
        return render(request, 'contest/cont_problem.html', context)


#To Show contest standings 
def contest_standings(request, cid):
    contest = Contest.objects.get(id=cid)
    context = { 'contest': contest }
    return render(request, 'contest/ranklist.html', context)






    
