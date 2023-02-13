from django.shortcuts import render

# Create your views here.

def index(request):
    # Home page
    return render(request, 'portfolios/index.html')

def projects(request):
    # Projects page
    return render(request, 'portfolios/projects.html')

def contact(request):
    # Contact page
    return render(request, 'portfolios/contact.html')

def about(request):
    # About page
    return render(request, 'portfolios/about.html')
