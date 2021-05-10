from django.shortcuts import render, redirect
from .models import Register
from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .decorators import unauthenticated_user, allowed_user, staff_only
from .forms import CreateUserForm
from django.contrib.auth.models import Group


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@unauthenticated_user
@csrf_protect
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('username')

            group = Group.objects.get(name='Customer')
            user.groups.add(group)

            messages.success(request, 'Account is Created successfully for ' + name)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register_l.html', context)


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def status(request):
    all_patient = Register.objects.all().order_by('oc')
    return render(request, 'status.html', {'all_patient': all_patient})


@login_required(login_url='login')
@staff_only
def staff_stat(request):
    all_patient = Register.objects.all().order_by('oc')
    return render(request, 'staff_stat.html', {'all_patient': all_patient})


@login_required(login_url='login')
def register_bed(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are added in waiting list')
            return render(request, 'home.html', {})
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            age = request.POST['age']
            mobile = request.POST['mobile']
            ct = request.POST['ct']
            oxy = request.POST['oxy']
            messages.success(request, 'There was error please try again ... ')
            return render(request, 'register.html', {'fname': fname, 'lname': lname, 'email': email, 'mobile': mobile, 'age': age, 'ct': ct, 'oxy': oxy})
    else:
        return render(request, 'register.html', {})

