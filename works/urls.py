from django.urls import path
from works import views

urlpatterns = [
    path('works/', views.works, name='works'),
]