from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password is Not Matching")
            return render(request, 'signup.html')                   
        try:
            # Check if the user already exists
            User.objects.get(username=email)
            messages.info(request, "Email is Taken")
            return render(request, 'signup.html')
        except User.DoesNotExist:
            # Create the user if it doesn't exist
            user = User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, "Signup Success")
            return redirect("/auth/login")  # Redirect to login page after successful signup
    return render(request, 'signup.html')

def handlelogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass1"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect("/")  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/auth/login")  # Redirect back to login page if login fails
    return render(request, "login.html")

def handlelogout(request):
    logout(request)
    return redirect('/auth/login')  # Redirect to login page after logout
