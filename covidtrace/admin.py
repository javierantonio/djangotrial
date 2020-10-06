from django.contrib import admin

# Register your models here.

from .models import Barangay, Citymun, Visitor, Sys_user, Establishment

admin.site.register(Barangay)
admin.site.register(Citymun)
admin.site.register(Visitor)
admin.site.register(Sys_user)
admin.site.register(Establishment)
