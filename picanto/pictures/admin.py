from django.contrib import admin

# Register your models here.

from . models import *


@admin.register(Customer)
class Customer_Admin(admin.ModelAdmin) :

   pass 

@admin.register(Customer_Picture)
class Customer_Pictures_Admin(admin.ModelAdmin) :

   pass 

@admin.register(Category)
class Customer_Category_Admin(admin.ModelAdmin) :

   pass

@admin.register(Comment)
class Customer_Comment_Admin(admin.ModelAdmin) :

   pass