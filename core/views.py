from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm
import re


 #### PATTERNS 
name_pattern = re.compile(r'[a-zA-Z]{2,}')
email_pattern = re.compile(r'[a-zA-Z0-9-.$_+]+@[a-zA-Z.-_]+\.[a-zA-Z-_.]+')
password_pattern = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{10,}$')


# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_check = request.POST['password_check']

        first_name_match = name_pattern.match(first_name)
        last_name_match = name_pattern.match(last_name)
        password_match = password_pattern.match(password)
        email_match = email_pattern.match(email)

        if password_match is not None:
            if password != password_check:
                messages.info(request, 'Password does not match')
                return redirect('signup')

            else:
                if first_name_match and last_name_match is not None:
                    if email_match is not None:
                        if User.objects.filter(username=email).exists():
                            messages.info(request, 'Account already exists')
                            return redirect('signup')
                            
                        else:
                            new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
                            new_user.save()
                            return redirect('login')
                         
                    else:
                        messages.info(request, 'Invalid Email')
                        return redirect('signup')       

                else:
                    messages.info(request, 'Invalid Name')
                    return redirect('signup')
                    
                    

        else:
            messages.info(request, 'Minimum 10 characters, at least 1 capital letter, 1 number and 1 special character')
            return redirect('signup')



    else:
        form = RegistrationForm()
        context = {
            'form' : form
        }

        return render(request, 'registration/signup.html', context)


@login_required(login_url='login')
def success(request):
    return render(request, 'success.html')