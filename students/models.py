from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(max_length=10)
    email = models.EmailField(unique=True, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.grade})"
    
    
class Teacher(models. Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.title