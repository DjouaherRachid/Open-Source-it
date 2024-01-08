from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from users.forms import UserCreationForm, UserChangeForm

# Register the User model in the Django admin interface
@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('id', 'username','first_name','last_name', 'email', 'last_login','date_joined','is_active','is_staff','is_superuser', 'role')

    list_filter = ('is_active','first_name','last_name', 'is_superuser','is_staff')

    readonly_fields = ['last_login','date_joined','created_at']

    search_fields = ('id', 'username', 'email')

    ordering = ('id', "username", "last_login")

    fieldsets = (
        ('User', {'fields': ('username',"first_name","last_name", 'email', 'password', 'role', 'groups')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
        ('Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2"),
        }),
    )    