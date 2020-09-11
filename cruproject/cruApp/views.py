from django.shortcuts import render,redirect
from cruApp.forms import EmployeeForm
from cruApp.models import Employee

# Create your views here.
def home_view(request):
    return render(request,'cruApp/home.html')

def retrive_view(request):
    list = Employee.objects.all()
    return render(request,'cruApp/index.html',{'list':list})

def insert_view(request):
    form = EmployeeForm()
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'cruApp/insert.html',{'form':form})

def delete_view(request,id):
    emplo = Employee.objects.get(id=id)
    emplo.delete()
    return redirect('/')


def update_view(request,id):
    emplo = Employee.objects.get(id=id)
    if request.method=='POST':
        form = EmployeeForm(request.POST,instance=emplo)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'cruApp/update.html',{'emplo':emplo})





