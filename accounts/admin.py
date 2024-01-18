from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CustomUserCreateForm
from .forms import CustomUserEditForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserEditForm
    list_display = ['username', 'first_name', 'last_name', 'email', 'birthday', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birthday',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
