from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='api-token-auth'),
    path('api-token/verify/', TokenVerifyView.as_view(), name='verify-token'),
    path('api-token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('admin/', admin.site.urls),
    path('', include('apps.parser.urls')),
    path('', include('apps.user_app.urls')),
]
