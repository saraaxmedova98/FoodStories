from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.forms import CustomUserCreationForm, CustomUserChangeForm
from account.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import  Group
from django.utils.safestring import mark_safe


admin.site.unregister(Group)

# Register your models here.

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'username', 'bio','profile_image', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    

    
admin.site.register(User, CustomUserAdmin)