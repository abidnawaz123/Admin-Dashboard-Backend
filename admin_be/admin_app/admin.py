from django.contrib import admin
from .models import *
from auth_user.models import User

admin.site.register(LatestCustomers)
admin.site.register(StudentDetailModel)
admin.site.register(StudentRecord)
admin.site.register(Furniture)
admin.site.register(HostelView)
admin.site.register(User)
