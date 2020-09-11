from django.contrib import admin
from ccApp.models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','ceo']

admin.site.register(Company,CompanyAdmin)

# username:- shakti
# password:- shakti123
# email:- shakti@gmail.com
