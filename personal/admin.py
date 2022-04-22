from django.contrib import admin

from .models import (
    User,
    Subscription,
)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass



