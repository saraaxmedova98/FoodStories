from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import CustomUser
from django.contrib.auth import get_user_model
# Register your forms here.

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

