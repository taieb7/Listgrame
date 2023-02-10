from datetime import date, datetime
from distutils.command.upload import upload
import email
from email.policy import default
from msilib.schema import Feature
from secrets import choice
from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Product Review


class Listing (models.Model):
    features = (

        ('Open Now', 'Open Now'),
        ('Near me', 'Near me'),
        ('Child Friendly', 'Child Friendly'),
        ('Free Parking', 'Free Parking'),
        ('Events', 'Events'),
        ('Free Wifi', 'Free Wifi'),






    )

    city = [
        ('Sfax', 'Sfax'),
        ('Sousse', 'Sousse'),
        ('Tunis', 'Tunis'),
        ('Monastir', 'Monastir'),
        ('Hammemat', 'Hammemat'),
        ('Mahdia', 'Mahdia'),




    ]
    category = [
        ('Restaurant', 'Restaurant'),
        ('Hotel', 'Hotel'),
        ('café', 'café'),
        ('Shopping', 'Shopping'),
        ('Fitness', 'Fitness'),
        ('Education', 'Education'),


    ]

    Listing_Title = models.CharField(max_length=100)
    Category = models.CharField(max_length=50, choices=category)
    Keywords = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Description = models.TextField(max_length=200)
    Features = MultiSelectField(choices=features, default='teacher')
    Gallery = models.ImageField(upload_to='photo/%y/%m/%d')
    city = models.CharField(max_length=50, choices=city)
    State = models.CharField(max_length=100)
    Zip_Code = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    Website = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Facebook_Link = models.CharField(max_length=100)
    Twitter_Link = models.CharField(max_length=100)
    Pinterest = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avg_rating = models.FloatField(max_length=100, default=0)
    post_views = models.IntegerField(default=0, null=True, blank=True)
    favourite = models.ManyToManyField(
        User, related_name='favourite', blank=True)
    Status = models.CharField(default='close', max_length=100)

    def get_absolute_url(self):
        return reverse('detail')


def __str__(self):
    return self.Listing_Title


class ListingReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    review_text = models.TextField()
    email = models.TextField()
    Gallery = models.ImageField(upload_to='Gallery/%y/%m/%d')
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150)
    message = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="customers/profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    """ @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')
    """


class days(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    Monday = models.JSONField()
    Tuesday = models.JSONField()
    Wednesday = models.JSONField()
    Thursday = models.JSONField()
    Friday = models.JSONField()
    Saturday = models.JSONField()
    Sunday = models.JSONField()
