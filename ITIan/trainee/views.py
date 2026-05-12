from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Trainee
from .forms import TraineeForm, TraineeModelForm


# ─── FUNCTION BASED VIEWS ────────────────────────────────────────────

# GET ALL (excludes soft deleted)
@login_required
def trainee_list(request):
    trainees = Trainee.objects.filter(is_deleted=False)
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

# GET BY ID
@login_required
def trainee_detail(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk, is_deleted=False)
    return render(request, 'trainee/trainee_detail.html', {'trainee': trainee})

# INSERT using plain Form with FK
@login_required
def add_trainee(request):
    form = TraineeForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        Trainee.objects.create(
            name   = form.cleaned_data['name'],
            email  = form.cleaned_data['email'],
            phone  = form.cleaned_data['phone'],
            course = form.cleaned_data['course'],
            image  = form.cleaned_data.get('image'),
        )
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_form.html', {'form': form, 'action': 'Add'})

# UPDATE
@login_required
def update_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    form = TraineeModelForm(request.POST or None, request.FILES or None, instance=trainee)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_form.html', {'form': form, 'action': 'Update'})

# HARD DELETE
@login_required
def delete_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_confirm_delete.html', {'trainee': trainee})

# SOFT DELETE
@login_required
def soft_delete_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        trainee.is_deleted = True
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/trainee_confirm_delete.html', {'trainee': trainee, 'soft': True})


# CLASS BASED VIEW (Insert) 

class AddTraineeCBV(View):
    def get(self, request):
        form = TraineeModelForm()
        return render(request, 'trainee/trainee_form.html', {'form': form, 'action': 'Add (CBV)'})

    def post(self, request):
        form = TraineeModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
        return render(request, 'trainee/trainee_form.html', {'form': form, 'action': 'Add (CBV)'})


# GENERIC VIEWS 

# Trainee List using Generic ListView
class TraineeListGeneric(ListView):
    model = Trainee
    template_name = 'trainee/trainee_list.html'
    context_object_name = 'trainees'

    def get_queryset(self):
        return Trainee.objects.filter(is_deleted=False)


# Trainee Insert using Generic CreateView + ModelForm
class TraineeCreateGeneric(CreateView):
    model = Trainee
    form_class = TraineeModelForm
    template_name = 'trainee/trainee_form.html'
    success_url = reverse_lazy('trainee_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['action'] = 'Add (Generic)'
        return ctx