from django.urls import path
from authentication import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

# URLs that include views for login, token refresh, registration, logout, and retrieving routes
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.getRoutes)
]