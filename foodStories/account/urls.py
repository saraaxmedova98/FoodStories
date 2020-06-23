from django.urls import path
from account.views import CreateRegisterView, UpdateUserView,UserLoginView, UserProfileView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('register/',CreateRegisterView.as_view(), name='register' ),
    path('login/',UserLoginView.as_view(), name='login' ),
    path('logout/',LogoutView.as_view(), name='logout' ),
    path("profile/", UserProfileView.as_view()  , name="user_profile"),
    path("update/<int:pk>", UpdateUserView.as_view(), name="update_user_info"),
]
