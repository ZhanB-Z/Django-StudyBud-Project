from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host','participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username','email','bio']  #this line shows what fields will be available/visible in the user-creation and user-update form