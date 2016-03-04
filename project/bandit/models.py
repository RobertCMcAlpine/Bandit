from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    
    TYPE_OPTIONS =(
                   ('B', 'Band'),
                   ('V', 'Venue'),
                   )
                   
    type = models.CharField(max_length=1, choices=TYPE_OPTIONS)
    website = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.user.username

class Band(models.Model):
    profile = models.OneToOneField(Profile)
    number_of_members = models.PositiveIntegerField()

    GENRE_OPTIONS = (
                    ("Alternative","Alternative"),
                     ("Blues/R&B","Blues/R&B"),
                     ("Childrens Music","Childrens Music"),
                     ("Classical","Classical"),
                     ("Country","Country"),
                     ("Dance","Dance"),
                     ("Easy Listening","Easy Listening"),
                     ("Electronic","Electronic"),
                     ("Folk","Folk"),
                     ("House","House"),
                     ("Industrial","Industrial"),
                     ("Techno","Techno"),
                     ("Trance","Trance"),
                     ("Hip Hop/Rap","Hip Hop/Rap"),
                     ("Holiday","Holiday"),
                     ("Jazz","Jazz"),
                     ("New Age","New Age"),
                     ("Pop","Pop"),
                     ("Religious","Religious"),
                     ("Rock","Rock"),
                     ("Soundtrack","Soundtrack"),
                     ("Unclassifiable","Unclassifiable"),
                     ("World","World"),
                    )
    genre = models.CharField(choices=GENRE_OPTIONS, max_length=128)

    def __unicode__(self):
        return self.profile.name

class Venue(models.Model):
    profile = models.OneToOneField(Profile)
    address = models.CharField(max_length=512)
    post_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.profile.name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    date = models.DateField()
# start time? end time? decide later
    start_time = models.TimeField()
    end_time = models.TimeField()
    reward = models.CharField(max_length=512)
    description = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name
