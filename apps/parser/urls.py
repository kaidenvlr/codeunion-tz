from django.urls import path

from apps.parser import views

urlpatterns = [
    path('currencies/', views.AllCurrencyViewSet.as_view({'get': 'list'}), name='currencies'),
    path('currency/<int:pk>/', views.CurrencyViewSet.as_view({'get': 'retrieve'}), name='currency'),
]
