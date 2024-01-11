from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from apartments.base_classes import UserPermissions
from users.serializers import UserSerializer
from users.models import User
from datetime import datetime

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [UserPermissions]

    def retrieve(self, request, pk=None):
        if request.user.has_perm('users.view_user'):
            return Response(UserSerializer(User.objects.get(pk=pk)).data, status=status.HTTP_200_OK)
        else:
            user = get_object_or_404(User.objects.all(), pk=pk)
            if user.username == request.user.username:
                serializer = self.serializer_class(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'status': 'unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request):
        try:
            u = User(
                username=request.data['username'],
                email=request.data['email'],
                role=request.data['role'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
            )
            u.set_password(request.data['password'])
            u.created_by = request.user

            u.save()

            return Response(UserSerializer(u).data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)