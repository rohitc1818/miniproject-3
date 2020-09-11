from django.contrib import admin
from cbApp.models import beer

# Register your models here.
class beerAdmin(admin.ModelAdmin):
    list_display = ['name','taste','color','price']

admin.site.register(beer,beerAdmin)

# username:- shankar
# password:- shankar123
# gmail:- shankar@gmail.com

