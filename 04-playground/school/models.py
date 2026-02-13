from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(100)]
    )
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='teacher')
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )
    course = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(11)]
    )
    
    def __str__(self):
        return self.name