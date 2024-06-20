from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from.forms import UserForm,UpdateUserForm
from django import forms

def home_view(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "registered successfully")
        return redirect('login')
    else:
        form=UserForm()
        return render(request, "registration/signup.html",{'form':form})



@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def edit_profile(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        if request.method == "POST":
            userform = UpdateUserForm(request.POST,instance=request.user)
            if userform.is_valid():
                print("hello")
                userform.save()
                messages.success(request, "profile updated successfully")
                return redirect('profile')
            else:
                print("failed validation")
                return render(request, 'registration/edit_profile.html', {'form': userform})
        else:
            form = UpdateUserForm(instance=current_user)
            return render(request, 'registration/edit_profile.html',{'form':form})
    else:
        return redirect('login')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('movie_list')
