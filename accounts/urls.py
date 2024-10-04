from django.urls import path
from .views import RegisterAPIView, LogoutAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
