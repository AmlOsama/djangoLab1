from django import forms
from .models import Trainee


class TraineeForm(forms.Form):
    from course.models import Course
    name   = forms.CharField(max_length=100)
    email  = forms.EmailField()
    phone  = forms.CharField(max_length=20)
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    image  = forms.ImageField(required=False)


class TraineeModelForm(forms.ModelForm):
    class Meta:
        model  = Trainee
        fields = ['name', 'email', 'phone', 'course', 'image']
        widgets = {
            'name':  forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }