from django.contrib import admin
from cruApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)


# username:- deo
# email:- deo@gmail.com
# password:- deo123


