from django.shortcuts import render

# Create your views here.
from app1.models import Junior, Middle, Senior


def junior(request):
    junior = Junior.objects.all()
    context = {'junior': junior}
    return render(request, 'junior.html', context)

def middle(request):
    middle = Middle.objects.all()
    context = {'middle': middle}
    return render(request, 'middle.html', context)

def senior (request):
    senior = Senior.objects.all()
    context = {'senior': senior}
    return render(request, 'senior.html', context)