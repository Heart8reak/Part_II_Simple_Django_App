from django.contrib import admin

# Register your models here.

from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_filter     = ['name','email','timestamp']
    list_display    = ['name','email','timestamp']

admin.site.register(Signup,SignupAdmin)