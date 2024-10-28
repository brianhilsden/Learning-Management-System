from django.urls import path
from .views import RegisterView,CustomTokenObtainPairView,UserProfileView,UsersListView,UserView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',RegisterView.as_view(), name="register" ),
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
    path('login/',CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(), name="token_refresh"),
    path('profile/',UserProfileView.as_view(),name='user_profile'),
    path('',UsersListView.as_view(),name='user-list'),

   
 
]