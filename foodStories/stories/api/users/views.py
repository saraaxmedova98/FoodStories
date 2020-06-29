from stories.models import Story, Recipe, Contact, Comment
from account.models import CustomUser
from stories.api.serializers import StoryModelSerializer, RecipeModelSerializer,UserModelSerializer,\
    ContactModelSerializer, CommentModelSerializer, RegistrationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from stories.api.users.serializers import UserSerializer

User = get_user_model()



class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
