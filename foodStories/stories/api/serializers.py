from rest_framework import serializers
from stories.models import Story, Recipe, Category, Comment, Contact, Subscribe
from account.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'bio', 'profile_image','is_staff','is_active', 'date_joined']
        # fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only = True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        def create(self, validated_data):
            user = User.objects.create(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                email = validated_data['last_name']
            )
            password = validated_data['password']
            user.set_password(password)
            user.save()
            return user
        


class StoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'title', 'description', 'story_image', 'cover_image', 'story_count', 'slug','category', 'user', 'updated_at','created_at']


class RecipeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        # fields = ['id', 'title', 'ingredients', 'prepare_time', 'recipe_image', 'cover_image', 'recipe_count','updated_at','created_at']
        fields= '__all__'
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id', 'title', 'image']
        fields= '__all__'


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ['id', 'name', 'email', 'message', 'commented_at']
        fields= '__all__'

class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # fields = ['id', 'name', 'email', 'subject', 'message','contacted_at']
        fields= '__all__'

class SubscribeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        # fields = ['id', 'email', 'subscribed_at']
        fields= '__all__'