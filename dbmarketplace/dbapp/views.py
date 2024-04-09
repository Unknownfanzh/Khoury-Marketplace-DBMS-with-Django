from django.shortcuts import render, redirect
from django.db import connection
from .forms import SQLQueryForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Allusers
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login
from django.utils import timezone

# from django.contrib.auth.decorators import login_required  # Ensure that only authenticated users can execute queries


def home(request):
    context = {'user': request.user}
    return render(request, 'home.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = Allusers.objects.get(username=username)
        except Allusers.DoesNotExist:
            # User not found
            return render(request, 'login.html', {'error_message': 'Username not found'})
        
        # Check if the password is correct
        # Here, `check_password` is used for demonstration. Your actual implementation might vary.
        if check_password(password, user.password):
            # Password is correct. Now, manually authenticate and login the user.
            # You might need to implement your custom method for logging in the user,
            # as Django's `login` requires a user instance that is compatible with its auth system.
            
            # For now, let's manually set the backend and call Django's login function.
            # This is not recommended for production without proper user model integration.
            user.backend = 'django.contrib.auth.backends.ModelBackend' # Specify the correct backend
            user.last_login = timezone.now()
            user.save(update_fields=['last_login'])
            auth_login(request, user)
            
            return redirect('home')
        else:
            # Password is incorrect
            return render(request, 'login.html', {'error_message': 'Password is incorrect'})
    else:
        # If not a POST request, display the login form
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    # Redirect to login page or home page
    return redirect('login')


def register(request):
    if request.method == 'POST':
        # Create a dictionary to simulate the serializer's input
        user_data = {
            'username': request.POST.get('username'),
            'fname': request.POST.get('first_name'),
            'lname': request.POST.get('last_name'),
            'password': make_password(request.POST.get('password')),  # Hash the password
            'isadmin': request.POST.get('is_admin', 'off') == 'on'  # Convert checkbox to boolean
        }

        # Now you have to manually validate and save the data
        # This is a simplified example; in a real scenario, you should validate the data thoroughly
        user = Allusers.objects.create(**user_data)

        # Redirect to login page after successful registration
        return redirect('login')
    else:
        # Render a registration form on GET request
        return render(request, 'register.html')


# @login_required
def run_query(request):
    if request.method == 'POST':
        form = SQLQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            with connection.cursor() as cursor:
                cursor.execute(query)
                # Fetch results if it's a SELECT statement, or provide a confirmation message otherwise
                if query.lower().startswith('select'):
                    rows = cursor.fetchall()
                else:
                    rows = [('Query executed successfully.',)]
            return render(request, 'query_results.html', {'form': form, 'rows': rows})
    else:
        form = SQLQueryForm()

    return render(request, 'run_query.html', {'form': form})
