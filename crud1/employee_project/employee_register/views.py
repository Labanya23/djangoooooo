from django.shortcuts import render, redirect
from .forms import EmployeeForm

# Create your views here.

def employee_list(request):
    return render(request,"employee_register/employee_list.html")

def employee_form(request):
    form = EmployeeForm()
    return render(request,"employee_register/employee_form.html",{'form': form})


def employee_(request):
    return
