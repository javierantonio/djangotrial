from django.contrib import admin

# Register your models here.

from .models import Barangay, Citymun

admin.site.register(Barangay)
admin.site.register(Citymun)
