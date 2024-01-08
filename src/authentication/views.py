from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import LoginSerializer, RegisterSerializer
from users.models import User

# Create your views here.

# Generate access and refresh tokens when a user logs in,
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

# Use the RegisterSerializer to validate and create a new user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
# Handle logout by invalidating the refresh token
@permission_classes([IsAuthenticated])
class LogoutView(APIView):

     def post(self, request):
        try:
            if request.data.get('all'):
                token: OutstandingToken
                for token in OutstandingToken.objects.filter(user=request.user):
                    _, _ = BlacklistedToken.objects.get_or_create(token=token)
                print("All refresh tokens blacklisted")
                return Response({"status": "All refresh tokens blacklisted"})
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(f'{e}')
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Return the available routes in the API 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/login/',
        '/api/register/',
        '/api/refresh-token/'
    ]
    return Response(routes)