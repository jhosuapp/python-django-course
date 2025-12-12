from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("days-by-number/<int:day>", views.days_week_with_number),
    path("days/<str:day>", views.days_week, name='day-quote')
]
