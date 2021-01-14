from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

router = DefaultRouter()

router.register('query', views.QueryModelViewSet, basename='query')


urlpatterns = [
    path('search', views.QueryAPIView.as_view(), name='search'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += router.urls
