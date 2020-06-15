from django.urls import path
from stories.views import home,about,login,register,single,reset_password,change_password,\
    forget_password,user_profile,email_subscribers,ContactView, SubscribeForm, RecipeList, \
    RecipeDetail, StoryList,StoryDetail, StoryView, LoginView

urlpatterns = [
    path('', home, name='home' ),
    path('about/', about, name='about' ),
    path('stories/', StoryList.as_view(), name='stories' ),
    path('stories/<int:pk>', StoryDetail.as_view(), name='story detail' ),
    path('recipes/', RecipeList.as_view(), name='recipes' ),
    path('recipes/<int:pk>', RecipeDetail.as_view(), name='recipe detail' ),
    path('contact/', ContactView.as_view() , name='contact' ),
    path('login/', LoginView.as_view(), name='login' ),
    path('register/', register, name='register' ),
    path('single/', single, name='single' ),
    path("reset_password/", reset_password, name="reset_password"),
    path("change_password/", change_password, name="change_password"),
    path("forget_password/", forget_password, name="forget_password"),
    path("user_profile/", user_profile, name="user_profile"),
    path("create_story/", StoryView.as_view(), name="create_story"),
    path("email_subscribers/", email_subscribers, name="email_subscribers")
    
]