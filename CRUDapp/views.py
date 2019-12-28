from django.shortcuts import render
from .form import StudentForm
from .models import Student


def index(request):
    form = StudentForm(request.POST)
    studentdata = Student.objects.all()
    context = {'form': form, 'studentdata': studentdata}
    return render(request, 'index.html', context)


def display(request):
    form = StudentForm(request.POST)
    form.save()
    studentdata = Student.objects.all()

    context = {'form': form, 'studentdata': studentdata}
    return render(request, 'index.html', context)


def update(request, sid):
    form = StudentForm(request.POST)
    studentdata = Student.objects.all()
    context = {'form': form, 'studentdata': studentdata}
    return render(request, 'edit.html', context)


def delete(request,sid):
    student = Student.objects.get(id=sid)
    student.delete()
    form = StudentForm(request.POST)
    studentdata = Student.objects.all()
    context = {'form': form, 'studentdata': studentdata}
    return render(request, 'index.html', context)
