from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def about(request):
    return render(request, 'portfolio/about_me.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def regression(request):
    return render(request, 'portfolio/regression.html')

def classification(request):
    return render(request, 'portfolio/classification.html')

def clustering(request):
    return render(request, 'portfolio/clustering.html')

def dimensionality_reduction(request):
    return render(request, 'portfolio/dimensionality_reduction.html')

