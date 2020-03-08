from django.shortcuts import render, redirect
from submission.models import Submission
from problem.models import Problem
from user.models import CustomUser
from django.contrib.auth.models import User


#To view all submissions
def status(request):
    all_sub = Submission.objects.all().order_by('-id') #descending order
    context = {'submission': all_sub}
    return render(request, 'status.html', context)

#To view own submissions 
def my_status(request):
    if request.user.is_authenticated :
       cuser = CustomUser.objects.get(id=request.user.id) # current_user
       f = {'user_id': cuser.id}
       my_sub = Submission.objects.filter(**f).order_by('-id') # descending order
       context = {'submission': my_sub}
       return render(request, 'status.html', context)
    else :
         return redirect('login')  
     
#To view last submission 
def single_status(request, pid):
    problem = Problem.objects.get(id=pid)
    cuser = CustomUser.objects.get(id=request.user.id) # current_user
    # pass two distinct value as map 
    # ref : https://stackoverflow.com/questions/51392868/passing-multiple-arguments-into-djangos-filter
    f = {'user_id': cuser.id, 'problem_id': pid}
    last_sub = Submission.objects.filter(**f).order_by('-id')[0]
    context = {'sub': last_sub}
    return render(request, 'single_status.html', context)




