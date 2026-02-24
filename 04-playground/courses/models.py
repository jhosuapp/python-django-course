from django.db import models

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    duration = models.IntegerField()
    teacher = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name='courses')
    students = models.ManyToManyField(Student, related_name="courses")
    categories = models.ManyToManyField(Category, related_name="courses")
    
