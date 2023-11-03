from django.urls import path

from apps.parser import views

urlpatterns = [
    path('currencies/', views.AllCurrencyAPIView.as_view(), name='currencies'),
    path('currency/<int:pk>/', views.CurrencyAPIView.as_view(), name='currency'),
]
