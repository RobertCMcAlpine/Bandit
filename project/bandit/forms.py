from django import forms
from django.contrib.auth.models import User
from bandit.models import Profile, Event, Band, Venue, get_image_path
from django.forms.extras.widgets import SelectDateWidget


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_type', 'name', 'profile_picture', 'city', 'phone_number', 'description')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'profile_picture', 'city', 'phone_number', 'description')

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name of the event:")
    date = forms.DateField(help_text="Please enter the date of the event:", input_formats=['%Y-%m-%d'], widget=SelectDateWidget)
    start_time = forms.TimeField(help_text="Please enter the start time of the event:")
    end_time = forms.TimeField(help_text="Please enter the end itme of the event:")
    reward = forms.CharField(max_length=128, help_text="Please enter the reward of the event:")
    description = forms.CharField(max_length=1024, help_text="Please enter a description for the event:")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Event
        fields = ('name', 'date', 'start_time', 'end_time', 'reward', 'description')



class BandForm(forms.ModelForm):
    class Meta():
        model = Band
        fields = ('number_of_members', 'genre')

class VenueForm(forms.ModelForm):
    class Meta():
        model = Venue
        fields = ('address', 'post_code')