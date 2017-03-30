from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import login, authenticate
from django.db import transaction

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# # Django transaction system so we can use @transaction.atomic
# from django.db import transaction

# # Imports the Item class
# from chatbot.models import Item

# # Imports the Posters class
# from chatbot.models import Posters

# # Import the Comments class
# from chatbot.models import Comment

# Imports the forms
from chatbot.forms import *

# Get the time
import datetime

# Import JSON
import json

# Used to generate a one-time-use token to verify a user's email address
from django.contrib.auth.tokens import default_token_generator

# Used to send mail from within Django
from django.core.mail import send_mail

# Action for the default /chatbot/ route.
@login_required()
# @ensure_csrf_cookie
def home(request):
    # Gets a list of all the posts in the database.
    # all_items = Item.objects.all()
    # all_comments = Comment.objects.all()
    # context = {'postform': AddForm(), 'posts': all_items, 'commentform': AddComment(), 'comments': all_comments}
    return render(request, 'chatbot/build_chat.html')


# Action for registering a User@transaction.atomic
def register(request):
    context = {}
    errors = []
    context['errors'] = errors
    # Just display the registration form if this is a GET request
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'chatbot/register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'chatbot/register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password1'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    # Mark the user as inactive to prevent login before email confirmation.
    new_user.is_active = False
    new_user.save()
    new_profile = Chatters()
    new_profile.username = new_user
    new_profile.save()
    new_profile.name = str(new_user)
    new_profile.save()

    # Generate a one-time use token and an email message body
    token = default_token_generator.make_token(new_user)

    email_body = str(new_user.first_name)+ """,
Welcome to the music information website Talk Music To Me!  Please click the link below to
verify your email address and complete the registration of your account:

  http://%s%s
""" % (request.get_host(), 
       reverse('confirm', args=(new_user.username, token)))

    send_mail(subject="Verify your email address",
              message= email_body,
              from_email="gosborne@andrew.cmu.edu",
              recipient_list=[new_user.email])

    context['email'] = form.cleaned_data['email']
    return render(request, 'chatbot/needs-confirmation.html', context)

# Action for sending to the Chatbot page
def chat(request):
    return render(request, 'chatbot/build_chat.html', {})

# Action for sending to the Explore page
def explore(request):
    return render(request, 'chatbot/build_explore.html', {})

# Action for sending to the Observer page
def observe(request):
    return render(request, 'chatbot/build_observe.html', {})

# Action for sending to the You page
def you(request):
    return render(request, 'chatbot/build_you.html', {})

# Action for sending to the settings
def settings(request):

    errors = []
    context = {}
    curr_user = request.user

    # Get the user information
    try:
        chatter = Chatters.objects.get(name = str(request.user.username))
    except ObjectDoesNotExist:
        errors.append('The profile does not exist.')

    context = {'chatter': chatter, 'errors': errors, 'form': EditForm(), 'cuser': curr_user}

    return render(request, 'chatbot/build_settings.html', context)

# Action for checkin if the user has successfully registered
@transaction.atomic
def confirm_registration(request, username, token):
    user = get_object_or_404(User, username=username)

    # Send 404 error if token is invalid
    if not default_token_generator.check_token(user, token):
        raise Http404

    # Otherwise token was valid, activate the user.
    user.is_active = True
    user.save()
    return render(request, 'chatbot/login.html', {})

# Action for sending to the email sent page
def needs_confirmation(request):
    return render(request, 'socialnetwork/needs-confirmation.html', {})

# Action for editing the user's profile
@login_required
def edit(request):

    errors = []
    context = {}
    curr_user = request.user

    # Get the user information
    try:
        chatter = Chatters.objects.get(name = str(request.user.username))
    except ObjectDoesNotExist:
        errors.append('The profile does not exist.')

    # Just display the edit form if this is a GET request
    if request.method == 'GET':
        context = {'chatter': chatter, 'errors': errors, 'form': EditForm(), 'cuser': curr_user}
        return redirect(reverse('settings'), context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = EditForm(request.POST)
    context['form'] = form

    if not form.is_valid():
        errors.append('Something you entered was not okay.')
        return render(request, 'chatbot/build_settings.html', context)

    # At this point, the form data is valid. Edit the user's information
    cuser = request.user
    chatter.age = form.cleaned_data['age']
    chatter.spotify =form.cleaned_data['spotify']
    chatter.save()

    context = {'chatter': chatter, 'errors': errors, 'form': EditForm(), 'cuser': curr_user}
    return render(request, 'chatbot/build_settings.html', context)


# Action for changing the photo
@login_required
def upload_pic(request, user_id):
    errors = []
    context = {}

    if request.method !='POST':
        errors.append('Uploading picture should be done with POST method')
    else:
        form = UploadImageForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            poster1 = Posters.objects.get(name = str(request.user.username))
            poster1.image = form.cleaned_data['image']
            poster1.save()
            return redirect(reverse('profile', kwargs={'user_id': user_id}))
        else:
            errors.append('Image was not valid.')

    return redirect(reverse('profile'), context)

