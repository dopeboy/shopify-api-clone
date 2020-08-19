from django.contrib import admin

from .models import User, Store, Purchase

admin.site.register(User)
admin.site.register(Store)
admin.site.register(Purchase)
# Register your models here.
