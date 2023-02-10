from unicodedata import name
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from app.forms import MyAuthForm

urlpatterns = [

    path('',  views.index, name='index'),
    path('all_category',  views.category, name='allCategory'),
    path('all_location',  views.location, name='alllocation'),
    path('add_listing',  views.listing, name='addlisting'),



    path('login',  views.loginn, name='login'),

    path('logout',  auth_views.LogoutView.as_view(
        template_name='registration/login.htm'), name='logout'),
    path('Dashboard',  views.Dashboard, name='Dashboard'),
    path('My_listing',  views.my_listing, name='my_listing'),
    path('my_profile',  views.my_profile, name='my_profile'),
    path('Reviews',  views.Reviews, name='Reviews'),
    path('add__listing',  views.Add_listing, name='add_listing'),
    path('favourites',  views.favourites, name='favourites'),
    path('about',  views.about, name='about'),
    path('contact',  views.contact, name='contact'),
    path('user_profile',  views.user_profile, name='user_profile'),
    path('all_category/<str:name>/', views.categori, name='categori'),
    path('all_location/<str:name>/', views.all_location, name='all_location'),
    path('search', views.search, name='search'),
    path('details/<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('favourite/<int:idd>', views.favourite, name='favourite'),
    path('Register',  views.Register, name='Register'),
    path('submit_review/<int:listing_id>/',
         views.submit_review, name='submit_review'),
    path('update/<int:id>', views.update, name='update'),
    path('favourite_delte/<int:id>', views.favourite_delte, name='favourite_delte'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('delete_reviews/<int:id>', views.delete_reviews, name='delete_reviews'),
    path('inbox',  views.inbox, name='inbox'),
    path('ShowNotifications/<int:id>',
         views.ShowNotifications, name='ShowNotifications'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
























]
