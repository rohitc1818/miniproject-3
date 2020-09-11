from django.shortcuts import render,redirect
from aaApp.forms import StudentForm
from aaApp.models import Student

# Create your views here.
def index_view(request):
    return render(request,'aaApp/index.html')

def home_view(request):
    form = StudentForm()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'aaApp/home.html',{'form':form})

def back_view(request):
    list = Student.objects.all()
    return render(request,'aaApp/back.html',{'list':list})

def delete_view(request,id):
    list = Student.objects.get(id=id)
    list.delete()
    return redirect('/back')

def update_view(request,id):
    list = Student.objects.get(id=id)
    if request.method=='POST':
        form = StudentForm(request.POST,instance=list)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'aaApp/update.html',{'list':list})







