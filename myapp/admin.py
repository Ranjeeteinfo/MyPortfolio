from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
@admin.register(Contact)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = [field.name for field in Contact._meta.fields]    