from dataclasses import fields
from logging import PlaceHolder
from site import USER_BASE
from socket import AddressInfo
from tkinter import Widget
from django import forms
from .models import Listing, ListingReview, Notification, Profile
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
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


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['Phone', 'Facebook_Link',
                  'Twitter_Link', 'Pinterest', 'State', 'Listing_Title', 'Longitude', 'Latitude', 'Zip_Code', 'Keywords',
                  'Address', 'Description', 'Gallery', 'Website', 'Category', 'city', 'Features']
        widgets = {
            'Listing_Title': forms.TextInput(attrs={'placeholder': 'Listing Title', 'class': "form-control filter-input"}),
            'Category': forms.Select(attrs={'placeholder': 'Category', 'class': "nice-select filter-input current"}, choices=category),
            'Keywords': forms.TextInput(attrs={'placeholder': 'Keywords', 'class': "form-control filter-input"}),
            'Address': forms.TextInput(attrs={'placeholder': 'Address', 'class': "form-control filter-input"}),
            'Description': forms.Textarea(attrs={'placeholder': 'Enter your text here', 'class': "form-control filter-input"}),
            'Gallery': forms.FileInput(attrs={'class': "add-listing__input-file"}),
            'city': forms.Select(attrs={'placeholder': 'city', 'class': "nice-select filter-input current"}, choices=city),
            'State': forms.TextInput(attrs={'placeholder': 'State', 'class': "form-control filter-input"}),
            'Zip_Code': forms.TextInput(attrs={'placeholder': 'Zip Code', 'class': "form-control filter-input"}),
            'Longitude': forms.TextInput(attrs={'placeholder': 'Longitude', 'class': "form-control filter-input"}),
            'Website': forms.TextInput(attrs={'placeholder': 'Website', 'class': "form-control filter-input"}),
            'Latitude': forms.TextInput(attrs={'placeholder': 'Latitude', 'class': "form-control filter-input"}),
            'Phone': forms.NumberInput(attrs={'placeholder': 'Phone', 'class': "form-control filter-input"}),
            'Facebook_Link': forms.TextInput(attrs={'placeholder': 'Facebook_Link', 'class': "form-control filter-input"}),
            'Twitter_Link': forms.TextInput(attrs={'placeholder': 'Twitter_Link', 'class': "form-control filter-input"}),
            'Pinterest': forms.TextInput(attrs={'placeholder': 'Pinterest', 'class': "form-control filter-input"}),








        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ListingReview
        fields = ['Gallery', 'review_text', 'rating', 'email']


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': "form-control"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Adresse', 'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'placeholder': 'first_name', 'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last_name', 'class': "form-control"}),


        }


class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password'].label = False


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['email', 'message']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'class': "form-control filter-input"}),
            'message': forms.Textarea(attrs={'placeholder': 'comment', 'class': "form-control filter-input"}),



        }


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msgs = ""
    for field in form:
        for error in field.errors:
            msgs += "%s: %s " % (field.label if hasattr(field,
                                                        'label') else 'Error', error)
    return msgs
