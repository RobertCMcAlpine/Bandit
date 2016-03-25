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
        fields = ('profile_type', 'name', 'profile_picture', 'city', 'phone_number', 'description', 'website')

        def clean(self):
            cleaned_data = self.cleaned_data
            website = cleaned_data.get('website')

            # If website is not empty and doesn't start with 'http://', prepend 'http://'.
            if website and not website.startswith('http://'):
                website = 'http://' + website
                cleaned_data['website'] = website

            return cleaned_data

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'profile_picture', 'city', 'phone_number', 'description', 'website')

        def clean(self):
            cleaned_data = self.cleaned_data
            website = cleaned_data.get('website')

            # If website is not empty and doesn't start with 'http://', prepend 'http://'.
            if website and not website.startswith('http://'):
                website = 'http://' + website
                cleaned_data['website'] = website

            return cleaned_data

class EventForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%Y-%m-%d'], widget=SelectDateWidget)
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