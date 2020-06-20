from django.urls import path
from stories.views import register,single,reset_password,change_password,\
    forget_password,user_profile,email_subscribers,ContactCreateView, SubscribeView, RecipeList, \
    RecipeDetail, StoryList,StoryDetail, StoryCreateView, StoryUpdateView, AboutView,\
         HomeView, StoryCategoryList, RecipeCategoriesList, RecipeCreateView, RecipeUpdateView, \
             RecipeDeleteView, StoryDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('about/', AboutView.as_view(), name='about' ),
    path('stories/', StoryList.as_view(), name='stories' ),
    path('stories/<int:pk>', StoryDetail.as_view(), name='story_detail' ),
    path("stories/<category>", StoryCategoryList.as_view(), name="story_category"),
    path("story/create", StoryCreateView.as_view(), name="create_story"),
    path("story/update/<int:pk>", StoryUpdateView.as_view(), name="update_story"),
    path('story/delete/<int:pk>', StoryDeleteView.as_view(), name='delete_story'),
    path('recipes/', RecipeList.as_view(), name='recipes' ),
    path('recipes/<int:pk>', RecipeDetail.as_view(), name='recipe_detail' ),
    path("recipes/<category>", RecipeCategoriesList.as_view(), name="recipe_category"),
    path('recipe/create', RecipeCreateView.as_view(), name='create_recipe'),
    path('recipe/update/<int:pk>', RecipeUpdateView.as_view(), name='update_recipe'),
    path('recipe/delete/<int:pk>', RecipeDeleteView.as_view(), name='delete_recipe'),
    path('contact/', ContactCreateView.as_view() , name='contact' ),
    # path('login/', LoginView.as_view(), name='login' ),
    path('register/', register, name='register' ),
    path('single/', single, name='single' ),
    path("reset_password/", reset_password, name="reset_password"),
    path("change_password/", change_password, name="change_password"),
    path("forget_password/", forget_password, name="forget_password"),
    path("user_profile/", user_profile, name="user_profile"),
    path("email_subscribers/", email_subscribers, name="email_subscribers"),
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    
    

    
]