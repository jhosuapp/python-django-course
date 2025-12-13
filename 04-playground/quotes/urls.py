from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='quotes'),
    path("days/<int:day>", views.days_week_with_number),
    path("days/<str:day>", views.days_week, name='day-quote')
]
