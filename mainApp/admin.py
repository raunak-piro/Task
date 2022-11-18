from django.contrib import admin
from mainApp.models import Buyer
from .models import Employee
from .models import Client
from .models import Project

admin.site.register(Buyer)
admin.site.register(Employee)

admin.site.register(Client)

admin.site.register(Project)

# Register your models here.
