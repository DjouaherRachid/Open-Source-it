from users.models import User
from apartments.base_classes import BaseSerializer


class UserSerializer(BaseSerializer):
    
    
    
    class Meta:
        model = User 
        fields = ("id", "username", "first_name", "last_name", "email", "last_login", "is_superuser",
                  "is_active", "date_joined", "created_at", "role") 

    
    def get_fields(self):
        fields = super().get_fields()
        exclude_fields = self.context.get('excluded_fields', [])
        
        
        for f in exclude_fields:
            if f in fields:
                fields.pop(f)

        return fields
