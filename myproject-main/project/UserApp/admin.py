from django.contrib import admin
from .models import UserMaster,ServiceProvider,Customer,Service
# Register your models here.
admin.site.register(UserMaster)
admin.site.register(Customer)
admin.site.register(ServiceProvider)
admin.site.register(Service)
