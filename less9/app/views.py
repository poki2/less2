from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register_visitor(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = RegistrationForm()

    return render(request, 'app/register.html', {'form': form})

def thankyou(request):
    return render(request, 'app/thankyou.html')