from django.contrib import admin
from .models import Customer,Payment,Subscription,Verification

# Register your models here.
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Subscription)
admin.site.register(Verification)
