from django.test import TestCase
from stories.models import Story, Category, Recipe, Contact, Subscribe
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class CategoryTest(TestCase):

    def create_category(self):
        user = User.objects.create(
            first_name='testing',
            last_name='testing', 
            email='testingging@gmail.com',
            )
        category = Category.objects.create(
            title='Category title'
            )
        return Category.objects.create(title='Category title')

    def test_check_category(self):
        create = self.create_category()
        self.assertTrue(create)

    def test_model_str(self):
        category = self.create_category()
        
        self.assertEqual(str(category), category.title)

class StoryTest(TestCase):

    def create_story(self):
        user = User.objects.create(
            first_name='testing',
            last_name='testing', 
            email='testingging@gmail.com',
            )
        category = Category.objects.create(
            title='testing'
            )
        return Story.objects.create(title='Story title',description='Description',story_image = 'stories/', category=category, user=user)

    def test_check_model(self):
        create = self.create_story()
        self.assertTrue(create)

    def test_model_str(self):
        story = self.create_story()
        
        self.assertEqual(str(story), story.title)



class RecipeTest(TestCase):

    def create_recipe(self):
        user = User.objects.create(
            first_name='testing',
            last_name='testing', 
            email='testingging@gmail.com',
            )
        category = Category.objects.create(
            title='testing'
            )
        return Recipe.objects.create(title='Recipe title',description='Description',ingredients='test', recipe_image = 'recipes/', category=category, user=user)

    def test_check_model(self):
        create = self.create_recipe()
        self.assertTrue(create)

    def test_model_str(self):
        recipe = self.create_recipe()
        
        self.assertEqual(str(recipe), recipe.title)


class ContactTest(TestCase):

    def create_contact(self):
        return Contact.objects.create(name='Name',email='“admin@gmail.com',subject='subject', message = 'message')

    def test_check_model(self):
        create = self.create_contact()
        self.assertTrue(create)

    def test_model_str(self):
        contact = self.create_contact()
        
        self.assertEqual(str(contact), contact.name)



class SubsciberTest(TestCase):

    def create_subscriber(self):
        return Subscribe.objects.create(email='admin@gmail.com')

    def test_check_model(self):
        create = self.create_subscriber()
        self.assertTrue(create)

    def test_model_str(self):
        subscriber = self.create_subscriber()
        
        self.assertEqual(str(subscriber), subscriber.email)