from django.urls import path
from skills import views

urlpatterns = [
    path('skills/', views.skills, name='skill'),
]