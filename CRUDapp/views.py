from django.http import JsonResponse
from django.shortcuts import render

from .serializers import StudentSerializer
from .form import StudentForm
from .models import Student
from django.views import View


class CRUDOps(View):
#     def getmodal(self): #never used - just for future reference
#         data = Student.objects.all()
#         modal = ""
#         for entry in data:
#             modal += " <tr><td>" + entry.eno + "</td><td>" + entry.name + "</td><td>" + entry.branch + "</td><td>"
#             modal += "<button class='editStudent' id='eStudent" + str(entry.id) + "' type='button'>Update</button>"
#             modal += "<button class='deleteStudent' id='dStudent" + str(entry.id) + "' type='button'>Delete</button>"
#             modal += "</td></tr>"

#         return modal

    def get(self, request):
        form = StudentForm(request.POST)

        studentdata = Student.objects.all()

        context = {'form': form, 'studentdata': studentdata}
        return render(request, 'index.html', context)
        # return JsonResponse(context)

    def post(self, request, sid=None):
        form = StudentForm(request.POST)

        if sid is not None:
            student = Student.objects.get(id=sid)
            form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()

        studentdata = Student.objects.all()

        context = {'form': form, 'studentdata': studentdata}
        return render(request, 'index.html', context)

    def put(self, request, sid):

        if sid is not None:
            studentdata = Student.objects.get(id=sid)

        return JsonResponse(StudentSerializer(studentdata).data, safe=False)

    def delete(self, request, sid):
        form = StudentForm(request.POST)
        student = Student.objects.get(id=sid)
        student.delete()
        studentdata = Student.objects.all()
        context = {'form': form, 'studentdata': studentdata}
        return render(request, 'index.html', context)
