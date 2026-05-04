from django.shortcuts import render , redirect , get_object_or_404
from .models import Trainee

def trainee_list(request):
    trainess =  Trainee.objects.all()
    return render (request, 'trainee/trainee_list.html',{'trainees':trainess})


def add_trainee(request):
    if request.method == 'POST':
        pass
    return render (request,'trainee/add_trainee.html')


def update_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        # handle update
        pass
    return redirect('trainee_list')


def delete_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    trainee.delete()
    return redirect('trainee_list')
# Create your views here.
