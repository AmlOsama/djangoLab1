from django.shortcuts import render ,redirect, get_object_or_404

from .models import Course

def course_list(request):
    courses =  Course.objects.all()
    return render (request, 'course/course_list.html',{'courses':courses})


def add_course(request):
    if request.method == 'POST':
        pass
    return render (request,'course/add_course.html')


def update_course(request, pk):
    trainee = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        # handle update
        pass
    return redirect('course_list')


def delete_course(request, pk):
    trainee = get_object_or_404(Course, pk=pk)
    trainee.delete()
    return redirect('course_list')
# Create your views here.



