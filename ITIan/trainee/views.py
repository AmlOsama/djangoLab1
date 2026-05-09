from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})


def trainee_detail(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    return render(request, 'trainee/trainee_detail.html', {'trainee': trainee})


def add_trainee(request):
    if request.method == 'POST':
        name  = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Trainee.objects.create(name=name, email=email, phone=phone)
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_form.html', {'action': 'Add'})


def update_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        trainee.name  = request.POST['name']
        trainee.email = request.POST['email']
        trainee.phone = request.POST['phone']
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_form.html', {'action': 'Update', 'trainee': trainee})


def delete_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        trainee.delete()   
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_confirm_delete.html', {'trainee': trainee})