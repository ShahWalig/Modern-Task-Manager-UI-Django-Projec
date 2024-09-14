from django.shortcuts import render, redirect
from .forms import CreateUserForms, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Render the homepage
def homepage(request):
    return render(request, "task_app/index.html")

# Handle user registration
def register(request):
    form = CreateUserForms()  # Initialize the registration form

    if request.method == "POST":
        form = CreateUserForms(request.POST)  # Bind form with POST data
        if form.is_valid():  # Check if form is valid
            form.save()  # Save the new user
            return redirect(my_login)  # Redirect to login page after successful registration

    context = {'registerform': form}  # Pass form to the template
    return render(request, "task_app/register.html", context)  # Render the registration page

# Handle user login
def my_login(request):
    form = LoginForm()  # Initialize the login form

    if request.method == "POST":
        form = LoginForm(data=request.POST)  # Bind form with POST data
        if form.is_valid():  # Check if form is valid
            username = form.cleaned_data.get("username")  # Get cleaned username
            password = form.cleaned_data.get("password")  # Get cleaned password
            user = authenticate(request, username=username, password=password)  # Authenticate the user

            if user is not None:  # If user is authenticated successfully
                auth.login(request, user)  # Log the user in
                return redirect('dashboard')  # Redirect to the dashboard

    context = {"loginform": form}  # Pass form to the template
    return render(request, "task_app/my-login.html", context)  # Render the login page

# Render the dashboard, requires login
@login_required(login_url='my_login')
def dashboard(request):
    return render(request, "task_app/dashboard.html")

# Handle user logout
def user_logout(request):
    auth.logout(request)  # Log the user out
    return redirect("my_login")  # Redirect to login page after logout
