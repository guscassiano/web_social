from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from register.views import RegisterModelView


router = DefaultRouter()
router.register('register', RegisterModelView)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterModelView.as_view({'get': 'list'}), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='api_token_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]