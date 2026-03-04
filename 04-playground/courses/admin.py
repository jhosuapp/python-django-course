# Register your models here.
from django.contrib import admin
from .models import Professor, Student, Category, Courses
# Register your models here.

class StudentInline(admin.TabularInline):
    model = Courses.students.through
    extra = 1

class ProfessorInline(admin.TabularInline):
    model = Courses
    extra = 1

class CoursesAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'description', 'teacher')
    
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    search_fields = ('username', 'email', 'phone')
    list_display = ('username', 'email', 'phone')
    
class ProfessortAdmin(admin.ModelAdmin):
    inlines = [ProfessorInline]
    search_fields = ('name',)
    list_display = ('name',)
        
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessortAdmin)
admin.site.register(Category)
