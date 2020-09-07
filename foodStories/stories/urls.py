from django.urls import path
from stories.views import *
from stories.api.urls import urlpatterns as api_urls


app_name = 'stories'

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('about/', AboutView.as_view(), name='about' ),
    path('stories/', StoryList.as_view(), name='stories' ),
    path('stories/filter', StoryFilterView.as_view(), name='story-filter' ),
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
    path("email_subscribers/", EmailSubscribeView.as_view(), name="email_subscribers"),
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("sum/", SumCreateView.as_view(), name="sum"),
    
] + api_urls