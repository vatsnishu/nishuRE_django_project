from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            #Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username alerady exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email alerady exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #login after register
                    # messages.success(request, 'You are now logged in')
                    # auth.login(request)
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Registration succesful, try logging in')
                    return redirect('login')
            return
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        #register user
        messages.error(request, 'testing')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        print('submitted_login')
        #login user
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
