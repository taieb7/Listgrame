from asyncio.windows_events import NULL
import datetime
from telnetlib import STATUS
from django.utils import timezone
from distutils import file_util
from email import message
from msilib import init_database
from msilib.schema import Condition, Feature
from multiprocessing import context
from pyexpat import features
from typing import Any
from django.shortcuts import redirect, render
from app.models import Listing, ListingReview, Notification, User, Profile, days
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ListingForm, NotificationForm, ReviewForm, UserRegistrationForm, form_validation_error
from django.db.models import Avg
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.views import View
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):

    allplaces = Listing.objects.all()
    Reviews = ListingReview.objects.all()
    now = datetime.datetime.now()
    daynow = now.strftime('%A')
    print(daynow)
    print(type(daynow))

    for allplaces in allplaces:
        alldays = days.objects.filter(listing_id=allplaces.id)
        for alldays in alldays:
            if daynow == "Monday":
                day = alldays.Monday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=allplaces.id).update(Status='open')
            elif daynow == 'Tuesday':
                day = alldays.Tuesday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=allplaces.id).update(Status='open')

            elif daynow == 'Wednesday':
                day = alldays.Wednesday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=allplaces.id).update(Status='open')
            elif daynow == 'Thursday':
                day = alldays.Thursday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=allplaces.id).update(Status='open')
            elif daynow == 'Friday':
                day = alldays.Friday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=allplaces.id).update(Status='open')
            elif daynow == "Saturday":
                day = alldays.Saturday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=allplaces.id).update(Status='open')

            elif daynow == 'Sunday':
                day = alldays.Sunday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=allplaces.id).update(Status='open')
    context = {
        'places': Listing.objects.filter(avg_rating=5),
        'allplaces': Listing.objects.all(),
        'Reviews': Reviews,
        'Fitness': Listing.objects.filter(Category='Fitness').count(),
        'Education': Listing.objects.filter(Category='Education').count(),
        'Hotel': Listing.objects.filter(Category='Hotel').count(),
        'Restaurant': Listing.objects.filter(Category='Restaurant').count(),
        'Shopping': Listing.objects.filter(Category='Shopping').count(),
        'café': Listing.objects.filter(Category='café').count(),

    }

    return render(request, 'pages/index.htm', context)


def category(request):

    context = {
        'Fitness': Listing.objects.filter(Category='Fitness').count(),
        'Education': Listing.objects.filter(Category='Education').count(),
        'Hotel': Listing.objects.filter(Category='Hotel').count(),
        'Restaurant': Listing.objects.filter(Category='Restaurant').count(),
        'Shopping': Listing.objects.filter(Category='Shopping').count(),
        'café': Listing.objects.filter(Category='café').count(),

    }
    return render(request, 'pages/All category.htm', context)

# Createreturn your views here.


def location(request):
    context = {
        'Sfax': Listing.objects.filter(city='Sfax').count(),
        'Tunis': Listing.objects.filter(city='Tunis').count(),
        'Monastir': Listing.objects.filter(city='Monastir').count(),
        'Mahdia': Listing.objects.filter(city='Mahdia').count(),
        'Sousse': Listing.objects.filter(city='Sousse').count(),
        'Hammemat': Listing.objects.filter(city='Hammemat').count(),

    }
    return render(request, 'pages/All location.htm', context)


def all_location(request, name):
    location = Listing.objects.filter(city=name)
    now = datetime.datetime.now()
    daynow = now.strftime('%A')
    for location in location:
        alldays = days.objects.filter(listing_id=location.id)
        for alldays in alldays:
            if daynow == "Monday":
                day = alldays.Monday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=location.id).update(Status='open')
            elif daynow == 'Tuesday':
                day = alldays.Tuesday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=location.id).update(Status='open')
            elif daynow == 'Wednesday':
                day = alldays.Wednesday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=location.id).update(Status='open')
            elif daynow == 'Thursday':
                day = alldays.Thursday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=location.id).update(Status='open')
            elif daynow == 'Friday':
                day = alldays.Friday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=location.id).update(Status='open')
            elif daynow == "Saturday":
                print('zzz')
                day = alldays.Saturday
                print(float(now.hour))
                print(day['open'])
                print(day['close'])
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=location.id).update(Status='open')

            elif daynow == 'Sunday':
                day = alldays.Sunday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=location.id).update(Status='open')
    paginator = Paginator(location, 2)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    context = {
        'product_list': product_list



    }
    return render(request, 'pages/search.htm', context)


def listing(request):
    form = ListingForm(request.POST, request.FILES)

    print(request.user.id)
    if form.is_valid():
        data = Listing()
        data.Phone = form.cleaned_data['Phone']
        data.Facebook_Link = form.cleaned_data['Facebook_Link']
        data.Twitter_Link = form.cleaned_data['Twitter_Link']
        data.Pinterest = form.cleaned_data['Pinterest']
        data.State = form.cleaned_data['State']
        data.Listing_Title = form.cleaned_data['Listing_Title']
        data.Longitude = form.cleaned_data['Longitude']
        data.Latitude = form.cleaned_data['Latitude']
        data.Zip_Code = form.cleaned_data['Zip_Code']
        data.Keywords = form.cleaned_data['Keywords']
        data.Address = form.cleaned_data['Address']
        data.Description = form.cleaned_data['Description']
        data.Gallery = form.cleaned_data['Gallery']
        data.Website = form.cleaned_data['Website']
        data.Category = form.cleaned_data['Category']
        data.city = form.cleaned_data['city']
        data.Features = form.cleaned_data['Features']
        data.user_id = request.user.id
        data.save()

        Mon = days.objects.create(
            Monday={'open': request.POST['Monday_open'],
                    'close': request.POST['Monday_close']},
            Tuesday={'open': request.POST['Tuesday_open'],
                     'close': request.POST['Tuesday_close']},
            Wednesday={'open': request.POST['Wednesday_open'],
                       'close': request.POST['Wednesday_close']},
            Thursday={'open': request.POST['Thursday_open'],
                      'close': request.POST['Thursday_close']},
            Friday={'open': request.POST['Friday_open'],
                    'close': request.POST['Friday_close']},
            Saturday={'open': request.POST['Saturday_open'],
                      'close': request.POST['Saturday_close']},
            Sunday={'open': request.POST['Sunday_open'],
                    'close': request.POST['Sunday_close']},
            listing_id=data.id


        )
        Mon.save()

    context = {'form': ListingForm



               }
    return render(request, 'pages/add_listing.htm', context)


def search(request):
    category = Listing.objects.all()
    if request.method == "POST":
        places = request.POST['places']
        categoryy = request.POST['category']
        search = request.POST['search']

        if search == '':
            category = Listing.objects.filter(Category=categoryy, city=places)

        if places == "Select Location":
            category = Listing.objects.filter(
                Category=categoryy, Listing_Title__icontains=search)
        if categoryy == "Select Categories":
            category = Listing.objects.filter(
                city=places, Listing_Title__icontains=search)
        if categoryy == "Select Categories" and search == '':
            category = Listing.objects.filter(city=places)
        if places == "Select Location" and search == '':
            category = Listing.objects.filter(
                Category=categoryy)
        if categoryy == "Select Categories" and places == "Select Location":
            category = Listing.objects.filter(Listing_Title__icontains=search)

        if places != "Select Location" and search != '' and categoryy != "Select Categories":
            category = Listing.objects.filter(
                Category=categoryy, city=places, Listing_Title__icontains=search)

    paginator = Paginator(category, 2)

    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    return render(request, 'pages/search.htm', {'product_list': product_list})


def categori(request, name):
    category = Listing.objects.filter(Category=name)
    paginator = Paginator(category, 2)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    now = datetime.datetime.now()
    daynow = now.strftime('%A')
    for category in category:
        alldays = days.objects.filter(listing_id=category.id)
        for alldays in alldays:
            if daynow == "Monday":
                day = alldays.Monday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=category.id).update(Status='open')
            elif daynow == 'Tuesday':
                day = alldays.Tuesday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=category.id).update(Status='open')
            elif daynow == 'Wednesday':
                day = alldays.Wednesday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=category.id).update(Status='open')
            elif daynow == 'Thursday':
                day = alldays.Thursday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=category.id).update(Status='open')
            elif daynow == 'Friday':
                day = alldays.Friday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=category.id).update(Status='open')
            elif daynow == "Saturday":
                day = alldays.Saturday

                if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=category.id).update(Status='open')

            elif daynow == 'Sunday':
                day = alldays.Sunday
                if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                    if float(day['open']) < float(now.hour) < float(day['close']):
                        Listing.objects.filter(
                            id=category.id).update(Status='open')

    return render(request, 'pages/search.htm', {'product_list': product_list})


def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('Dashboard')

        elif user is not None:
            login(request, user)
            return redirect('index')

        else:
            msgg = 'Please enter a correct username and password'
            return render(request, 'registration/login.htm', {'msgg': msgg})

    return render(request, 'registration/login.htm')


@staff_member_required
def Dashboard(request):
    count_notifications = None
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            is_seen=False).count()
    all_user = User.objects.filter(is_superuser='False')
    users = User.objects.filter(is_superuser='False').count()

    alll_isting = Listing.objects.all().count()
    all_reviews = ListingReview.objects.all().count()
    most_views = Listing.objects.all().order_by('-post_views')[:3]
    all_views = Listing.objects.aggregate(Sum('post_views'))
    all_viewss = 0
    if all_views['post_views__sum'] != None:
        all_viewss = int(all_views['post_views__sum'])

    context = {
        'alll_isting': alll_isting,
        'all_reviews': all_reviews,
        'all_views': all_viewss,
        'most_views': most_views,
        'all_user': all_user,
        'count_notifications': count_notifications,
        'users': users


    }

    return render(request, 'admin/Dashboard.htm', context)


def contact(request):
    form = NotificationForm()
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        print('bbbb')
        if form.is_valid():
            print('oiooi')
            data = Notification()
            data.email = form.cleaned_data['email']
            print(data.email)
            data.message = form.cleaned_data['message']
            print(data.message)

            data.user_id = request.user.id
            print(data.user_id)

            data.save()
    return render(request, 'pages/contact_us.htm', {'form': form})


def ShowNotifications(request, id):
    Notification.objects.filter(id=id, is_seen=False).update(is_seen=True)
    return redirect('inbox')


@staff_member_required
def inbox(request):
    notifications = Notification.objects.all().order_by('-date')
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            is_seen=False).count()

    context = {
        'count_notifications': count_notifications,
        'notifications': notifications


    }

    return render(request, 'admin/inbox.htm', context)


@staff_member_required
def my_listing(request):
    all_listings = Listing.objects.all()
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            is_seen=False).count()
        context = {
            'count_notifications': count_notifications,
            'all_listings': all_listings


        }
    return render(request, 'admin/My_listing.htm', context)


@staff_member_required
def my_profile(request):
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            is_seen=False).count()
        context = {
            'count_notifications': count_notifications,


        }
    return render(request, 'admin/my_profile.htm', context)


def Reviews(request):
    Reviews = ListingReview.objects.all()
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            is_seen=False).count()
        context = {
            'count_notifications': count_notifications,
            'Reviews': Reviews


        }
    return render(request, 'admin/Reviews.htm', context)


def Add_listing(request):
    form = ListingForm(request.POST, request.FILES)
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            is_seen=False).count()

    if form.is_valid():
        data = Listing()
        data.Phone = form.cleaned_data['Phone']
        data.Facebook_Link = form.cleaned_data['Facebook_Link']
        data.Twitter_Link = form.cleaned_data['Twitter_Link']
        data.Pinterest = form.cleaned_data['Pinterest']
        data.State = form.cleaned_data['State']
        data.Listing_Title = form.cleaned_data['Listing_Title']
        data.Longitude = form.cleaned_data['Longitude']
        data.Latitude = form.cleaned_data['Latitude']
        data.Zip_Code = form.cleaned_data['Zip_Code']
        data.Keywords = form.cleaned_data['Keywords']
        data.Address = form.cleaned_data['Address']
        data.Description = form.cleaned_data['Description']
        data.Gallery = form.cleaned_data['Gallery']
        data.Website = form.cleaned_data['Website']
        data.Category = form.cleaned_data['Category']
        data.city = form.cleaned_data['city']
        data.Features = form.cleaned_data['Features']

        data.user_id = request.user.id
        data.save()
    context = {'form': ListingForm,
               'count_notifications': count_notifications,

               }
    return render(request, 'admin/add_listing.htm', context)


def favourites(request):
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            is_seen=False).count()

    user = request.user
    fav = user.favourite.all()
    context = {


        'fav': fav,
        'count_notifications': count_notifications,



    }

    return render(request, 'admin/favourites.htm', context)


def about(request):
    return render(request, 'pages/about_us.htm')


@login_required(login_url='/app/login')
def user_profile(request):
    profile = None
    if Profile.objects.get_or_create(user_id=request.user.id) != NULL:
        profile = Profile.objects.get(user_id=request.user.id)
    listings = Listing.objects.filter(user_id=request.user.id)
    user = request.user
    fav = user.favourite.all()
    filter = ListingReview.objects.none()
    for listings in listings:
        Reviews = ListingReview.objects.filter(listing_id=listings.id)
        filter = filter | Reviews
    listings = Listing.objects.filter(user_id=request.user.id)

    context = {
        'listings': listings,
        'Reviews': filter,
        'fav': fav,
        'profile': profile

    }

    return render(request, 'pages/user_profile.htm', context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('app')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("registration/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on \
                received activation link to confirm and complete the registration.')
    else:
        messages.error(
            request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))

            return redirect('Register')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.htm', {'form': form})


def detail(request, id):
    pp = Listing.objects.get(id=id)
    hours = days.objects.filter(listing_id=id)
    now = datetime.datetime.now()
    daynow = now.strftime('%A')
    etats = 'close'

    for hours in hours:

        if daynow == "Monday":
            day = hours.Monday
            if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                if float(day['open']) < float(now.hour) < float(day['close']):
                    etats = 'open'
        elif daynow == 'Tuesday':
            day = hours.Tuesday
            if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                if float(day['open']) < float(now.hour) < float(day['close']):
                    etats = 'open'
        elif daynow == 'Wednesday':
            day = hours.Wednesday
            if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                if float(day['open']) < float(now.hour) < float(day['close']):
                    etats = 'open'
        elif daynow == 'Thursday':
            day = hours.Thursday
            if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                if float(day['open']) < float(now.hour) < float(day['close']):
                    etats = 'open'
        elif daynow == 'Friday':
            day = hours.Friday
            if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                if float(day['open']) < float(now.hour) < float(day['close']):
                    etats = 'open'
        elif daynow == "Saturday":
            day = hours.Saturday
            if day['open'] != "Opening Time" and day['close'] != "Closing Time":

                if float(day['open']) < float(now.hour) < float(day['close']):
                    etats = 'open'

        elif daynow == 'Sunday':
            day = hours.Sunday
            if day['open'] != "Opening Time" and day['close'] != "Closing Time":
                if float(day['open']) < float(now.hour) < float(day['close']):
                    etats = 'open'

    if not request.user.is_superuser:

        pp.post_views = pp.post_views + 1
        pp.save()

    Reviews = ListingReview.objects.filter(listing_id=id)
    reviews = Reviews.aggregate(Avg('rating'))
    avg = 0
    if reviews['rating__avg'] is not None:
        avg = float(reviews['rating__avg'])
        avgg = (f'{avg:.1f}')
        pp.avg_rating = avgg
        pp.save()

    CountReview = Reviews.count()
    is_favourite = False

    if pp.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    category = Listing.objects.filter(Category=pp.Category, city=pp.city)

    context = {
        'Reviews': Reviews,
        'pp': pp,
        'avg': avg,
        'CountReview': CountReview,
        'category': category,
        'is_favourite': is_favourite,
        'hours': hours,
        'daynow': daynow,
        'etats': etats

    }
    return render(request, 'pages/details.htm', context)


def submit_review(request, listing_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            data = ListingReview()
            data.email = form.cleaned_data['email']
            data.rating = form.cleaned_data['rating']
            data.review_text = form.cleaned_data['review_text']
            data.Gallery = form.cleaned_data['Gallery']
            data.listing_id = listing_id
            data.user_id = request.user.id
            data.save()
            return redirect('detail', id=listing_id)


@staff_member_required
def delete(request, id):
    pi = Listing.objects.get(id=id)
    pi.delete()
    all_listings = Listing.objects.all()
    return render(request, 'admin/My_listing.htm', {'all_listings': all_listings})


@login_required(login_url='/app/login')
def favourite(request, idd):
    fav = Listing.objects.get(id=idd)
    if fav.favourite.filter(id=request.user.id).exists():
        fav.favourite.remove(request.user)
    else:
        fav.favourite.add(request.user)
    return redirect('detail', id=idd)


def update(request, id):
    mymember = Listing.objects.get(id=id)
    form = ListingForm(instance=mymember)
    if request.method == 'POST':
        form = ListingForm(request.POST,  request.FILES, instance=mymember)
        if form.is_valid():
            form.save()
            return redirect('my_listing')

    context = {
        'form': form,
    }
    return render(request, 'admin/update.htm', context)


def favourite_delte(request, id):
    fav = Listing.objects.get(id=id)
    fav.favourite.remove(request.user)
    return redirect('favourites')


def delete_reviews(request, id):
    p = ListingReview.objects.get(id=id)
    pp = Listing.objects.get(id=p.listing_id)
    p.delete()
    Reviewss = ListingReview.objects.filter(listing_id=pp.id)
    reviews = Reviewss.aggregate(Avg('rating'))
    avg = 0
    if reviews['rating__avg'] is not None:
        avg = float(reviews['rating__avg'])
        avgg = (f'{avg:.1f}')
        pp.avg_rating = avgg
        pp.save()
    else:
        pp.avg_rating = avg
        pp.save()

    Reviews = ListingReview.objects.all()
    return render(request, 'admin/Reviews.htm', {'Reviews': Reviews})


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'pages/profile.htm', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)
        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))

        return redirect('profile')


def error_404_view(request, exception):
    return render(request, 'pages/404_page.htm')
