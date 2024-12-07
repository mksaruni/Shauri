from django.shortcuts import render, redirect

#from students.models import Student
#from . serializers import StudentSerializer
#from rest_framework import viewsets


# Create your views here.
def index(request):
    return render(request, 'index.html')

def layout(request):
    return render(request, 'layout.html')

def insertdata(request):
    if request.method == "POST":

         name = request.POST['name']
         email = request.POST['email']
         age = request.POST['age']
         number = request.POST['number']
         image = request.FILES['image']

         student = Student(name=name, email=email, age=age, number=number, image=image)
         student.save()
         return redirect("/")

     return render(request, 'insert.html')
#
# def insertdata(request):
#     if request.method == "POST":
#
#         name = request.POST['name']
#         email = request.POST['email']
#         age = request.POST['age']
#         number = request.POST['number']
#         image = request.FILES['image']
#
#         student = Student(name=name, email=email, age=age, number=number, image=image)
#         student.save()
#         return redirect("/")
#
#     return render(request, 'insert.html')
#
 def viewdata(request):
   students = Student.objects.all()
    return render(request, 'viewdata.html', {"students": students})
#
# def edit(request, id):
#     if request.method == "POST":
#
#         name = request.POST['name']
#         email = request.POST['email']
#         age = request.POST['age']
#         number = request.POST['number']
#         image = request.FILES['image']
#
#         student = Student.objects.get(id=id)
#
#         student.name = name
#         student.email = email
#         student.age = age
#         student.number = number
#         student.image = image
#
#         student.save()
#         return redirect("/viewdata")
#
#     student = Student.objects.get(id=id)
#     return render(request, 'edit.html', {"student": student} )
#
# def details(request, id):
#     student = Student.objects.get(id=id)
#     return render(request, 'details.html', {"student": student} )
#
 def delete(request, id):
     student = Student.objects.get(id=id)
     student.delete()
     return redirect("/viewdata")
#
# class StudentView(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
