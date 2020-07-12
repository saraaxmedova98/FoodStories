from django.test import TestCase, Client
from django.urls import reverse
from stories.models import Contact, Story, Category
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User=get_user_model()

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_home_view(self):
        url = reverse("stories:home")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='index.html')



class StoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_story_view(self):
        url = reverse("stories:stories")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='stories.html')


class RecipeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_story_view(self):
        url = reverse("stories:recipes")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='recipes.html')


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_story_view(self):
        url = reverse("stories:contact")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, template_name='contact.html')

 
        
        request_data = {
            'name': 'Your Name',
            'email': 'admin@gmail.com',
            'subject': 'your subject',
            'message': 'message'
        }

        response = self.client.post(url , request_data)

        self.assertEqual(response.status_code, 302)


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    
    def test_story_view(self):
        url = reverse("account:login")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='registration/login.html')

        request_data = {
            'username': 'admin@gmail.com',
            'password': 'tech_academy'
        }
        # user = authenticate(request_data)
        
        response = self.client.post(url , request_data)

        # self.assertEqual(response.status_code, 302)
        # self.assertTrue(self.user.is_active)



class StoryDetailViewTest(TestCase):
    
    def setUp(self):
        self.story = Story.objects.create(
            title='Story title',
            description='Description',
            story_image = 'stories/', 
            )
        
    def test_story_detail_view(self):
        url = reverse("stories:story_detail", args=(self.story.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
        self.assertTemplateUsed(response, template_name='story_detail.html')



# class UserProfileViewTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             first_name='testing',
#             last_name='testing', 
#             email='testingging@gmail.com',
#             )

    
#     def test_user_profile_view(self):
#         url = reverse("account:user_profile", args=(self.user.pk,))
#         resp = self.client.get(url)

#         self.assertEqual(resp.status_code, 200)

#         self.assertTemplateUsed(resp, template_name='about.html')


class CreateStoryViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title='testing'
            )
        self.story = Story.objects.create(title='Story title',description='Description',story_image = 'stories/', category=self.category)

 
    def test_create_story_view(self):
        url = reverse("stories:create_story")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, template_name='create_story.html')

        # contact = Contact.objects.last()
        # print(contact)
        
        request_data = {
            'title':'Story title',
            'description':'Description',
            'story_image' : 'stories/',
            'category':self.category
        }

        response = self.client.post(url , request_data)

        # self.assertEqual(response.status_code, 302)



class StoryUpdateViewTest(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(title='testing'
            )
        self.story = Story.objects.create(
            title='Story title',
            description='Description',
            story_image = 'stories/', 
            )
        
    def test_story_detail_view(self):
        url = reverse("stories:update_story", args=(self.story.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
        self.assertTemplateUsed(response, template_name='create_story.html')


        request_data = {
            'title':'Story title',
            'description':'Description',
            'story_image' : 'stories/',
            'category': self.category
        }

        response = self.client.post(url , request_data)

        # self.assertEqual(response.status_code, 302)


class StoryDeleteViewTest(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(title='testing'
            )
        self.story = Story.objects.create(
            title='Story title',
            description='Description',
            story_image = 'stories/', 
            )
        
    def test_story_detail_view(self):
        url = reverse("stories:delete_story", args=(self.story.pk,))

        request_data = {
            'title':'Story title',
            'description':'Description',
            'story_image' : 'stories/',
            'category': self.category
        }

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)

        self.assertTrue(self.story)
