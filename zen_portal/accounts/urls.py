from django.urls import path
from .views import UserCreateView, UserListView

urlpatterns = [
    path('account_register/', UserCreateView.as_view(), name='account-register'),
    path('account/', UserListView.as_view(), name='account-list'),
]