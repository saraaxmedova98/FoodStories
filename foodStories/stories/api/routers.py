from rest_framework.routers import DefaultRouter
from stories.api.views import StoryViewSet, UserViewSet, RecipeViewSet

router = DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/stories', StoryViewSet)
router.register(r'api/recipes', RecipeViewSet)