from rest_framework import serializers
from rest_framework.permissions import DjangoObjectPermissions

class CustomPermission(DjangoObjectPermissions):
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

class BaseSerializer(serializers.ModelSerializer):
    def get_fields(self):
        fields = super().get_fields()
        exclude_fields = self.context.get('excluded_fields', [])
        
        
        for f in exclude_fields:
            if f in fields:
                fields.pop(f)

        return fields
    
    
class UserPermissions(CustomPermission):
    def has_permission(self, request, view):
        if view.action == "forms" or view.action == "retrieve" or view.action == "contacts":
            return True
        return super().has_permission(request, view)