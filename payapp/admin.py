from django.contrib import admin
from .models import Customer,Payment,Verification

# Register your models here.
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Verification)
