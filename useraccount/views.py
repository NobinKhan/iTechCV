from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.
def login(request):
    try:
        if request.method != 'POST':
            return render(request, 'accounts/login.html')
        else:
            #  collect User information
            loginusername = request.POST['username']
            loginpassword = request.POST['password']

            # validating user information
            user = auth.authenticate(username=loginusername, password=loginpassword)

            # saving user information
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect('dashboard')
            else:
                messages.error(request, "Username or Password is not matched. Please try again !")
                return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect('index')