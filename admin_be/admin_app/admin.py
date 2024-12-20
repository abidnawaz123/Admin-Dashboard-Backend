from django.contrib import admin
from .models import *
from auth_user.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(LatestCustomers)
admin.site.register(StudentDetailModel)
admin.site.register(StudentRecord)
admin.site.register(Furniture)
admin.site.register(HostelView)
admin.site.register(User,UserAdmin)
