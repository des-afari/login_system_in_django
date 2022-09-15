from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def signup(request):
    form = RegistrationForm()
    context = {
        'form' : form
    }

    return render(request, 'registration/signup.html', context)