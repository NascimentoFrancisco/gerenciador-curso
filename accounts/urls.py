from django.urls import path
from .views import CustomUserCreate, LoginUser, LogoutUser

app_name = "accounts"

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name='create_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/',LogoutUser.as_view(),name='logout'),
              
]