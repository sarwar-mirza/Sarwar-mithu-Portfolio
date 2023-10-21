from django.shortcuts import render

# home views here.
def home(request):
    
    return render(request, 'portfolio/home.html')
