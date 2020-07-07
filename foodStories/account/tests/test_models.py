# from django.test import TestCase
# from stories.models import Story, Category
# from account.models import CustomUser
# from django.contrib.auth import get_user_model

# Create your tests here.

# User = get_user_model()

# class StoryTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create(
#             first_name='hawking',
#             last_name='hawking', 
#             email='hawking@gmail.com',
#             )
        # self.user.save()
        # self.category = Category.objects.create(
        #     title='test'
        #     )
        # self.category.save()
        # self.story = Story.objects.create(
        #     title='hawking', 
        #     category=self.category , 
        #     user = self.user)
        # self.story.save()

    # def test_str_is_equal_to_title(self):
    #     """
    #     Method `__str__` should be equal to field `title`
    #     """
    #     story = Story.objects.filter(pk=2)
    #     print(story)
    #     self.assertEqual(story.__str__(), 'salam')