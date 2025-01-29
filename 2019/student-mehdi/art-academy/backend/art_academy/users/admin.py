from django.contrib import admin
from .models import Profile, Payment, PaymentType


admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(PaymentType)
