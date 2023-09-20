from django.shortcuts import render

# Create your views here.


def project_concept(request):
    return render(request, 'index.html')