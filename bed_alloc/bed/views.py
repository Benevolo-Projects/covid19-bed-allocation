from django.shortcuts import render, redirect
from .models import Register
from .forms import RegisterForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def status(request):
    all_patient = Register.objects.all
    return render(request, 'status.html', {'all_patient': all_patient})


def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
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
        messages.success(request, 'You are added in waiting list')
        return redirect('home')
    else:
        return render(request, 'register.html', {})

