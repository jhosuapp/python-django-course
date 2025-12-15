from django.shortcuts import render

# Create your views here.

def course_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Principiante',
            'rating': 4.8,
            'instructor': 'Alison Walsh',
            'course_title': 'Python: fundamentos hasta los detalles',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg',
        },
        {
            'id': 2,
            'level': 'Avanzado',
            'rating': 4.0,
            'instructor': 'Patty Kutch',
            'course_title': 'Beginner"s Guide to Successful Company Management: Business And More',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/20.jpg',
        },
        {
            'id': 3,
            'level': 'Principiante',
            'rating': 4.8,
            'instructor': 'Alonzo Murray',
            'course_title': 'Python: fundamentos hasta los detalles',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/men/32.jpg',
        },
        {
            'id': 4,
            'level': 'Principiante',
            'rating': 4.8,
            'instructor': 'Gregory Harris',
            'course_title': 'Python: fundamentos hasta los detalles',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/45.jpg',
        },
    ]
    
    response = {
        'courses': courses
    }
    
    return render(request, 'courses/courses.html', response)

def course_detail(request):
    return render(request, 'courses/courses_detail.html')

def course_lessons(request):
    return render(request, 'courses/courses_lessons.html')