from django.contrib import admin
from aaApp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','school','ranl','age','marks']

admin.site.register(Student,StudentAdmin)

# username:- shikari
# password:-shikari123
# gmail:- shikari@gmail.com

