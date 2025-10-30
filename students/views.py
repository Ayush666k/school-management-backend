from django.shortcuts import render, redirect
from .models import Student, Teacher, Course
# from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, filters
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
# @login_required(login_url='login')
# def list_students(request):
#     q = request.GET.get('q', '')
#     students = Student.objects.all()
#     if q:
#         students = students.filter(
#             name__icontains=q
#         )
#     return render(request, 'students/list.html', {'students':students , 'search_query': q})

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view_students')
#     else:
#         form = StudentForm()
#     return render(request, 'students/add_student.html', {'form': form})

# def update_student(request, id):
#     student = Student.objects.get(id=id)
#     form = StudentForm(request.POST or None, instance=student)
#     if form.is_valid():
#         form.save()
#         return redirect('view_students')
#     return render(request, 'Students/add_student.html', {'form':form})

# def delete_student(request, id):
#     student = Student.objects.get(id=id)
#     if request.method == 'POST':
#         student.delete()
#         return redirect('view_students')
    
#     return render(request, 'students/delete_confirm.html', {'student': student})

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['grade', 'age']
    search_fields = ['name', 'email']
    ordering_fields = ['age', 'name']
    
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['subject']
    search_fields = ['name', 'subject', 'email']
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['teacher']
    search_fields = ['title', 'description']
    
def dashboards(request):
    return render(request, 'students/dashboards.html')
    
    









