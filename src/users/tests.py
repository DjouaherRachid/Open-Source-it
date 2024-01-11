from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib import admin

from users.admin import UserAdmin
from users.forms import UserCreationForm, UserChangeForm

class UserAdminTest(TestCase):
    def test_user_admin_should_be_registered(self):
        # Vérifiez si l'UserAdmin est bien enregistré dans l'interface d'administration
        self.assertIn(get_user_model(), admin.site._registry)

    def test_user_admin_should_use_correct_forms(self):
        # Vérifiez si l'UserAdmin utilise les formulaires UserCreationForm et UserChangeForm
        user_admin = UserAdmin(get_user_model(), admin.site)
        self.assertEqual(user_admin.add_form, UserCreationForm)
        self.assertEqual(user_admin.form, UserChangeForm)

    def test_user_admin_should_have_correct_list_display(self):
        # Vérifiez si l'UserAdmin a les bons champs dans list_display
        expected_list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'role')
        user_admin = UserAdmin(get_user_model(), admin.site)
        self.assertEqual(user_admin.list_display, expected_list_display)
