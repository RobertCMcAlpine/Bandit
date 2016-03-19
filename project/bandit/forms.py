from django import forms
from django.contrib.auth.models import User
from bandit.models import Profile, Event

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'city', 'profile_type')

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name of the event.")
    date = forms.DateField(help_text="Please enter the date of the event.")
    start_time = forms.TimeField(help_text="Please enter the start time of the event.")
    end_time = forms.TimeField(help_text="Please enter the end itme of the event.")
    reward = forms.CharField(max_length=128, help_text="Please enter the reward of the event.")
    description = forms.CharField(max_length=1024, help_text="Please enter a description for the event.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Event
        fields = ('name', 'date', 'start_time', 'end_time', 'reward', 'description')