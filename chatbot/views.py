# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.utils import timezone

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# # Django transaction system so we can use @transaction.atomic
# from django.db import transaction

# # Imports the Item class
from chatbot.models import *

# Imports the forms
from chatbot.forms import *

# Get the time
import datetime

# Import JSON
import json

# Import requests
import requests

# Used to generate a one-time-use token to verify a user's email address
from django.contrib.auth.tokens import default_token_generator

# Used to send mail from within Django
from django.core.mail import send_mail

#Setup Spotipy Account - in terminal

# __init__(auth=, cleint_credentials
# export SPOTIPY_CLIENT_ID='ba6790bdcd434f06b7b577e344c6e0ae'
# export SPOTIPY_CLIENT_SECRET='145715e565ff48469c306484896a34f5'
# export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

import sys
import spotipy
import spotipy.util as util
import base64
import urllib
import urllib2

state_key = 'GZ2TPEFHXMB4'

def spotify_callback(request):
    return render(request, 'chatbot/spotify_loggedin.html', {})

# Action for loggin in step and giving a greeting.
@login_required()
def login_step(request):

    errors = []

    #  Trying to get the login form here...
    if request.method == 'POST':
        print("we at least got a post")


    new_mess = Mess(text="Hello there! Welcome to Talk Music To Me! My name is Botto. How can I help you find something to listen to today?",
                    user=request.user,
                    created=timezone.now(),
                    reality_coefficient=False
                    )
    new_mess.save()

    # Deletes the user's Spotify token so we will auto-update it upon getting to the chat page
    try:
        chatter = Chatters.objects.get(name = str(request.user.username))
        chatter.spotify_auth = '0'
        chatter.save()
    except ObjectDoesNotExist:
        errors.append('The profile does not exist.')

    return redirect(reverse('home'))

# Action for responding to something the user says
@login_required()
def respond_chat(request):

    new_mess = Mess(text="Response template.",
                    user=request.user,
                    created=timezone.now(),
                    reality_coefficient=False
                    )
    new_mess.save()
    mess = Mess.objects.all()
    response_text = serializers.serialize('json', Mess.objects.all())
    return HttpResponse(response_text, content_type='application/json')

# Action for the default /chatbot/ route.
@login_required()
# @ensure_csrf_cookie
def home(request):
    # Gets a list of all the messages in the database.
    context = {'form': EditForm()}
    return render(request, 'chatbot/build_settings.html', context)


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
    new_profile.fname = new_user.first_name
    new_profile.lname = new_user.last_name
    new_profile.email = new_user.email
    new_profile.save()
    new_profile.location =form.cleaned_data['location']
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

    # Just display the registration form if this is a GET request
    if request.method == 'GET':
        context = {'form': EditForm(), 'cuser': curr_user}
        return render(request, 'chatbot/build_settings.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = EditForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        context = {'form': EditForm(), 'cuser': curr_user}
        return render(request, 'chatbot/build_settings.html', context)

        # Get the user information
    try:
        chatter = Chatters.objects.get(name = str(request.user.username))
    except ObjectDoesNotExist:
        errors.append('The profile does not exist.')

    # Form is valid!
    if (len(form.cleaned_data['first_name']) > 0):
        chatter.fname = form.cleaned_data['first_name']
        chatter.save()
    elif (len(form.cleaned_data['last_name']) > 0):
        chatter.lname = form.cleaned_data['last_name']
        chatter.save()
    elif (len(form.cleaned_data['age']) > 0):
        chatter.age = form.cleaned_data['age']
        chatter.save()
    elif (len(form.cleaned_data['email']) > 0):
        chatter.email = form.cleaned_data['email']
        chatter.save()
    elif (len(form.cleaned_data['location']) > 0):
        chatter.location = str(form.cleaned_data['location'])
        chatter.save()

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
    return render(request, 'chatbot/needs-confirmation.html', {})


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
        context = {'form': EditForm(), 'cuser': curr_user}
        return render(request, 'chatbot/build_settings.html', context)

    # At this point, the form data is valid. Edit the user's information
    cuser = request.user
    chatter.age = form.cleaned_data['age']
    chatter.spotify =form.cleaned_data['spotify']
    chatter.save()

    context = {'chatter': chatter, 'errors': errors, 'form': EditForm(), 'cuser': curr_user}
    return render(request, 'chatbot/build_settings.html', context)

# Action for adding a message to the chat.
@login_required
def add_chat(request):

    errors = []

    if not 'item' in request.POST or not request.POST['item']:
        message = 'You must enter an item to add.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    new_mess = Mess(text=request.POST['item'],
                    user=request.user,
                    created=datetime.datetime.now(),
                    reality_coefficient=True
                    )
    new_mess.save()
    mess = Mess.objects.all()
    response_text = serializers.serialize('json', Mess.objects.all())
    return HttpResponse(response_text, content_type='application/json')

# Action for adding specific information to the observe tab
@login_required
def add_observe(request):

    errors = []

    if not 'item' in request.POST or not request.POST['item']:
        message = 'You must enter an item to add.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')


    stringout = str(request.POST['item'])
    string1 = stringout.split('~', 1)

    searchval =  string1[0]
    string2 = string1[1].split('~', 1)
    searchtype = string2[0]
    searchparam = string2[1]

    if searchtype == "Tag":
        search_tag(request, searchparam, searchval)
    elif searchtype== "Location":
        search_location(request, searchparam)
    else:
        print("Failure: Did not search by Tag or Location.")    

    response_text = serializers.serialize('json', Mess.objects.all())
    return HttpResponse(response_text, content_type='application/json')


# Action for adding all the personal top information to the you tab
@login_required
def add_you(request):

    errors = []

    # Delete previous search objects
    # SearchRes.objects.all().delete()
    # ArtistRes.objects.all().delete()
    # GenreRes.objects.all().delete()
    # PlaylistRes.objects.all().delete()

    chatter = Chatters.objects.get(name = str(request.user.username))
    chatter.toptracks.all().delete()
    chatter.topartists.all().delete()
    chatter.topgenres.all().delete()

    auth_token = chatter.spotify_auth
    sp = spotipy.Spotify(auth=auth_token)
    result = sp.current_user_top_tracks()

    count = 0

    # print json.dumps(result, indent=6, sort_keys=True) # Pretty Print
    # Find the user's top tracks   

    for track in result['items'][:10]:

        if (len(track['album']['images']) > 0):
            imagelink = track['album']['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_track = Tracks(track=track['name'],
                           artist=track['artists'][0]['name'],
                           album=track['album']['name'],
                           img=imagelink,
                           created=timezone.now(),
                           index = count,
                           popularity = track['popularity'],
                           uri=track['uri'],
                           top_tracks = chatter
                           )
        features = sp.audio_features(str(track['uri'].split(':')[2]))
        new_track.acousticness = features[0]['acousticness']
        new_track.danceability = features[0]['danceability']
        new_track.energy = features[0]['energy']
        new_track.instrumentalness = features[0]['instrumentalness']
        new_track.key = features[0]['key']
        new_track.liveness = features[0]['liveness']
        new_track.loudness = features[0]['loudness']
        new_track.speechiness = features[0]['speechiness']
        new_track.tempo = features[0]['tempo']
        new_track.time_signature = features[0]['time_signature']
        new_track.valence = features[0]['valence']


        new_track.save()
        count = count + 1


    result = sp.current_user_top_artists()

    count = 0
    # print json.dumps(result, indent=6, sort_keys=True) # Pretty Print
    # Find the users top artists, determine genres

    for artist in result['items'][:10]:

        if (len(artist['images']) > 0):
            imagelink = artist['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_artist = Artists(artist=artist['name'],
                             uri = artist['uri'],
                             popularity = artist['popularity'],
                             img = imagelink,
                             created = timezone.now(),
                             top_artists = chatter,
                             index = count
                             )
        new_artist.save()
        count = count + 1

        genres = artist['genres']
        length = len(genres)

        genrelist = chatter.topgenres.all()

        for genre in genres[:length]:

            if(len(genrelist.filter(genre=genre)) == 1):
                addgenre = genrelist.get(genre=genre)
                addgenre.number = addgenre.number + 1
                addgenre.save()
            else:
                new_genre = Genres(genre = genre,
                                   created = timezone.now(),
                                   top_genres = chatter,
                                   number = 1
                                  )
                new_genre.save()

    # genrelist = chatter.topgenres.all()
    # genrelist.filter(number__lte=2).delete()

    # Determine user's aggregate metadata
    tracklist = chatter.toptracks.all()
    count = 0

    for track in tracklist:
        chatter.acousticness = chatter.acousticness + tracklist[count].acousticness
        chatter.danceability = chatter.danceability + tracklist[count].danceability
        chatter.energy = chatter.energy + tracklist[count].energy
        chatter.instrumentalness = chatter.instrumentalness + tracklist[count].instrumentalness
        chatter.key = chatter.key + tracklist[count].key
        chatter.liveness = chatter.liveness + tracklist[count].liveness
        chatter.loudness = chatter.loudness + tracklist[count].loudness
        chatter.speechiness = chatter.speechiness + tracklist[count].speechiness
        chatter.tempo = chatter.tempo + tracklist[count].tempo
        chatter.time_signature = chatter.time_signature + tracklist[count].time_signature
        chatter.valence = chatter.valence + tracklist[count].valence
        chatter.save()
        count = count + 1

    chatter.acousticness = chatter.acousticness/count
    chatter.danceability = chatter.danceability/count
    chatter.energy = chatter.energy/count
    chatter.instrumentalness = chatter.instrumentalness/count
    chatter.key = chatter.key/count
    chatter.liveness = chatter.liveness/count
    chatter.loudness = chatter.loudness/count
    chatter.speechiness = chatter.speechiness/count
    chatter.tempo = chatter.tempo/count
    chatter.time_signature = chatter.time_signature/count
    chatter.valence = chatter.valence/count
    chatter.save()

    response_text = serializers.serialize('json', Mess.objects.all())
    return HttpResponse(response_text, content_type='application/json')

# Action for adding the spotify authentication token
@login_required
def add_spotify_token(request):

    errors = []

    if not 'item' in request.POST or not request.POST['item']:
        message = 'No token was received.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    chatter = Chatters.objects.get(name = str(request.user.username))
    chatter.spotify_auth = request.POST['item']
    chatter.save()

    mess = Mess.objects.all()
    response_text = serializers.serialize('json', Mess.objects.all())
    return HttpResponse(response_text, content_type='application/json')

# Action for the /socialnetwork/add-item route.
@login_required
def add_explore(request):

    errors = []

    if not 'item' in request.POST or not request.POST['item']:
        message = 'You must enter an item to add.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    stringout = str(request.POST['item'])
    string1 = stringout.split('%', 1)

    searchparam =  string1[1]
    searchval = string1[0]

    if searchparam == "Artist":
        search_artist(request, searchval)
    elif searchparam == "Track":
        search_track(request, searchval)
    elif searchparam == "Genre":
        search_genre(request, searchval)
    elif searchparam == "Playlist":
        search_playlist(request, searchval)
    else:
        print("Failure")

    # print(request.POST['select'])

    # new_mess = Mess(text=request.POST['item'],
    #                 user=request.user,
    #                 created=datetime.datetime.now(),
    #                 reality_coefficient=True
    #                 )
    # new_mess.save()
    # mess = Mess.objects.all()

    response_text = serializers.serialize('json', ArtistRes.objects.all())
    return HttpResponse(response_text, content_type='application/json')


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

# Action for logging out and deleting all messages for that particular user
@login_required
def logout_step(request):

    guy = User.objects.get(username__iexact = str(request.user.username))
    Mess.objects.filter(user=guy).delete()

    return redirect(reverse('logout'))

# Action for using Ajax to automatically update chat content
@login_required
def get_list_json(request):
    guy1 = serializers.serialize('json', Mess.objects.filter(user = request.user))
    guy2 = serializers.serialize('json', Chatters.objects.filter(name = str(request.user.username)))
    guys = {'mess': guy1, 'chatter': guy2}
    out = json.dumps(guys)

    return HttpResponse(out, content_type='application/json')

# Action for using Ajax to automatically update search content
@login_required
def get_explore_json(request):
    guy1 = serializers.serialize('json', SearchRes.objects.filter(user = request.user))
    guy2 = serializers.serialize('json', ArtistRes.objects.filter(user = request.user))
    guy4 = serializers.serialize('json', GenreRes.objects.filter(user = request.user))
    guy5 = serializers.serialize('json', PlaylistRes.objects.filter(user = request.user))
    guy3 = serializers.serialize('json', Chatters.objects.filter(name = str(request.user.username)))
    guys = {'search': guy1, 'search_artist': guy2, 'chatter': guy3, 'search_genre': guy4, 'search_playlist': guy5}
    out = json.dumps(guys)

    return HttpResponse(out, content_type='application/json')

# Action for using Ajax to automatically update search content
@login_required
def get_observe_json(request):
    guy1 = serializers.serialize('json', SearchRes.objects.filter(user = request.user))
    guy2 = serializers.serialize('json', Chatters.objects.all())
    guy4 = serializers.serialize('json', hotTracks.objects.all())
    guy3 = serializers.serialize('json', Chatters.objects.filter(name = str(request.user.username)))
    guys = {'search': guy1, 'chatters': guy2, 'chatter': guy3, 'htracks': guy4}
    out = json.dumps(guys)

    return HttpResponse(out, content_type='application/json')

# Action for using Ajax to automatically update you content
@login_required
def get_you_json(request):
    chatter = Chatters.objects.get(name = str(request.user.username))
    guy1 = serializers.serialize('json', chatter.toptracks.all())
    guy2 = serializers.serialize('json', chatter.topartists.all())
    guy4 = serializers.serialize('json', chatter.topgenres.all())
    guy3 = serializers.serialize('json', Chatters.objects.filter(name = str(request.user.username)))
    guys = {'tracks': guy1, 'artists': guy2, 'chatter': guy3, 'genres': guy4}
    out = json.dumps(guys)

    return HttpResponse(out, content_type='application/json')

# Action for using Ajax to automatically update you city
@login_required
def get_city_json(request):

    loc = dict(locations)
    countlist = []
    for i in range(0, 380):
        countlist.append(len( Chatters.objects.all().filter(location=str(i)) ))

    chatter = Chatters.objects.get(name = str(request.user.username))
    guy1 = serializers.serialize('json', Chatters.objects.filter(name = str(request.user.username)))
    loc.update({'chatter': guy1, 'countlist': countlist})
    out = json.dumps(loc)

    return HttpResponse(out, content_type='application/json')

# More ajax automatic serealization
@login_required
def get_list_xml(request):
    response_text = serializers.serialize('xml', Mess.objects.all())
    return HttpResponse(response_text, content_type='application/xml')

@login_required
def get_list_xml_template(request):
    context = { 'mess': Mess.objects.all() }
    return render(request, 'jquery_todolist/items.xml', context, content_type='application/xml')





# Spotify Functions

# Logging in the user business

# token = util.prompt_for_user_token(username)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     playlists = sp.user_playlists(username)
#     for playlist in playlists['items']:
#         print(playlist['name'])
# else:
#     print("Can't get token for", username)

# Searching for an artist
# Returns : a JSON, comprising of albums by the arist, tracks, and
# metadata for all of it. Finds the artist URI.
def search_artist(request, search_str):

    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    ArtistRes.objects.filter(user = request.user).delete()
    GenreRes.objects.filter(user = request.user).delete()
    PlaylistRes.objects.filter(user = request.user).delete()
    

    sp = spotipy.Spotify()
    result = sp.search(search_str, type='artist')  # result contains data in JSON format

    num = len(result['artists']['items'])
       
    for item in result['artists']['items'][:num]:

        if (len(item['images']) > 0):
            imagelink = item['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_search = ArtistRes(artist=item['name'],
                               user = request.user,
                               uri = item['uri'],
                               popularity = item['popularity'],
                               img = imagelink,
                               created = timezone.now()
                               )
        new_search.save()

# Searching for an artist
# Returns : a JSON, comprising of albums by the arist, tracks, and
# metadata for all of it. Finds the artist URI.
def search_track(request, search_str):

    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    ArtistRes.objects.filter(user = request.user).delete()
    GenreRes.objects.filter(user = request.user).delete()
    PlaylistRes.objects.filter(user = request.user).delete()

    sp = spotipy.Spotify()
    result = sp.search(search_str, type='track')  # result contains data in JSON format

    # print json.dumps(result, indent=6, sort_keys=True)

    num = len(result['tracks']['items'])
       
    for item in result['tracks']['items'][:num]:

        if (len(item['album']['images']) > 0):
            imagelink = item['album']['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_search = SearchRes(track=item['name'],
                               user = request.user,
                               artist=item['artists'][0]['name'],
                               album=item['album']['name'],
                               img=imagelink,
                               created=timezone.now(),
                               popularity = item['popularity'],
                               uri=item['uri']
                               )
        new_search.save()

# Searching for a playlist
def search_playlist(request, search_str):

    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    ArtistRes.objects.filter(user = request.user).delete()
    GenreRes.objects.filter(user = request.user).delete()
    PlaylistRes.objects.filter(user = request.user).delete()

    sp = spotipy.Spotify()
    result = sp.search(search_str, type='playlist')

    # print json.dumps(result, indent=6, sort_keys=True)

    for item in result['playlists']['items']:
        if (len(item['images']) > 0):
            imagelink = item['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        ownerid = item['owner']['id']
        ownerresult = sp.user(ownerid)

        # print json.dumps(ownerresult, indent=6, sort_keys=True)

        if(ownerresult['display_name']):
            ownername = ownerresult['display_name']
        else:
            ownername = ownerresult['id']

        new_search = PlaylistRes(playlist = item['name'],
                                 user = request.user,
                                 img = imagelink,
                                 owner = ownername,
                                 ownerid = ownerresult['id'],
                                 created = timezone.now(),
                                 uri = item['uri'],
                                 followers = ownerresult['followers']['total'],
                                 trackcount = item['tracks']['total']
                                )
        new_search.save()

# Searching for a genre
def search_genre(request, search_str):

    # Delete all previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    ArtistRes.objects.filter(user = request.user).delete()
    GenreRes.objects.filter(user = request.user).delete()
    PlaylistRes.objects.all().filter(user = request.user).delete()

    chatter = Chatters.objects.get(name = str(request.user.username))

    auth_token = chatter.spotify_auth

    sp = spotipy.Spotify(auth=auth_token)
    results = sp.recommendation_genre_seeds()

    # print json.dumps(results, indent=6, sort_keys=True)
    ind = []
    i = 0;

    for item in results['genres']:
        if (item == search_str.lower()):
            ind = i
        i = i + 1

    if (ind):
        genre = str(results['genres'][ind])
        results = sp.recommendations(seed_genres=[genre])
        # print json.dumps(results, indent=6, sort_keys=True)

        num = len(results['tracks'])
       
        for item in results['tracks'][:num]:

            if (len(item['album']['images']) > 0):
                imagelink = item['album']['images'][0]['url']
            else:
                imagelink = '../../static/img/egg.png'

            new_search = ArtistRes(artist=item['artists'][0]['name'],
                                   user = request.user,
                                   uri = item['artists'][0]['uri'],
                                   popularity = item['popularity'],
                                   img = imagelink,
                                   created = timezone.now()
                                   )
            new_search.save()

    else:
        new_search = GenreRes(genre='Try one of these:',
                              user = request.user,
                              created = timezone.now()
                              )
        new_search.save()

        for item in results['genres']:
            new_search = GenreRes(genre=item,
                                  user = request.user,
                                  created = timezone.now()
                                  )
            new_search.save()

# View for searching by tag and parameter
def search_tag(request, searchparam, searchval):

    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    chatter = Chatters.objects.get(name = str(request.user.username))
    auth_token = chatter.spotify_auth

    sp = spotipy.Spotify(auth=auth_token)
    result = sp.search(searchval, type='track')  # result contains data in JSON format

    # print json.dumps(result, indent=6, sort_keys=True)

    num = len(result['tracks']['items'])
       
    for item in result['tracks']['items'][:num]:

        if (len(item['album']['images']) > 0):
            imagelink = item['album']['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_search = SearchRes(track=item['name'],
                               user = request.user,
                               artist=item['artists'][0]['name'],
                               album=item['album']['name'],
                               img=imagelink,
                               created=timezone.now(),
                               popularity = item['popularity'],
                               uri=item['uri']
                               )
        new_search.save()
        features = sp.audio_features(str(new_search.uri.split(':')[2]))
        new_search.acousticness = features[0]['acousticness']
        new_search.danceability = features[0]['danceability']
        new_search.energy = features[0]['energy']
        new_search.instrumentalness = features[0]['instrumentalness']
        new_search.key = features[0]['key']
        new_search.liveness = features[0]['liveness']
        new_search.loudness = features[0]['loudness']
        new_search.speechiness = features[0]['speechiness']
        new_search.tempo = features[0]['tempo']
        new_search.time_signature = features[0]['time_signature']
        new_search.valence = features[0]['valence']
        new_search.save()

# View for searchign by location
def search_location(request, searchloc):

    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    locdict = dict(locations)

    locid = ''
    for i in range(0, 380):
        if (searchloc == locdict[str(i)].split(',')[0]):
            locid = str(i)

    areausers = Chatters.objects.filter(location = locid)
    hotTracks.objects.filter(location=locid).delete()

    for usr in areausers:
        for track in usr.toptracks.all():

            if (len( hotTracks.objects.filter(location=locid, uri=track.uri) ) < 1):

                new_track = hotTracks(track =track.track,
                                      artist=track.artist,
                                      album=track.album,
                                      img=track.img,
                                      created=timezone.now(),
                                      popularity = track.popularity,
                                      uri=track.uri,
                                      location=locid,
                                      duplicates = 1
                                   )
                new_track.save()
                new_track.acousticness = track.acousticness
                new_track.danceability = track.danceability
                new_track.energy = track.energy
                new_track.instrumentalness = track.instrumentalness
                new_track.key = track.key
                new_track.liveness = track.liveness
                new_track.loudness = track.loudness
                new_track.speechiness = track.speechiness
                new_track.tempo = track.tempo
                new_track.time_signature = track.time_signature
                new_track.valence = track.valence
                new_track.save()

            else:
                new_track = hotTracks.objects.get(location=locid, uri=track.uri)
                new_track.duplicates = new_track.duplicates + 1
                new_track.save()


# View for calling search_genre through a link
def search_artist_with_genre(request):
    if not 'item' in request.POST or not request.POST['item']:
        message = 'Must pass a genre to the Spotify API.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    genre = str(request.POST['item'])

    search_genre(request, genre)

    response_text = serializers.serialize('json', GenreRes.objects.all())
    return HttpResponse(response_text, content_type='application/json')


# Top ten tracks for an artist
def artist_top_ten(request):

    if not 'item' in request.POST or not request.POST['item']:
        message = 'Artist must have a URI to pass to the Spotify API.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    uri = str(request.POST['item'])

    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    ArtistRes.objects.filter(user = request.user).delete()
    GenreRes.objects.filter(user = request.user).delete()
    PlaylistRes.objects.filter(user = request.user).delete()

    spotify = spotipy.Spotify()
    results = spotify.artist_top_tracks(uri)

    # print json.dumps(results, indent=6, sort_keys=True) # Pretty Print

    for track in results['tracks'][:10]:

        if (len(track['album']['images']) > 0):
            imagelink = track['album']['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_search = SearchRes(track=track['name'],
                               user = request.user,
                               artist=track['artists'][0]['name'],
                               album=track['album']['name'],
                               img=imagelink,
                               created=timezone.now(),
                               popularity = track['popularity'],
                               uri=track['uri']
                               )
        new_search.save()

    response_text = serializers.serialize('json', SearchRes.objects.all())
    return HttpResponse(response_text, content_type='application/json')

# Finding relavent track for recommendations
def recommend_track(request):

    if not 'item' in request.POST or not request.POST['item']:
        message = 'Track must have a URI to pass to the Spotify API.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    stringout = request.POST['item'].encode('utf-8')
    string1 = stringout.split('~', 1)

    uri =  string1[0]
    string2 = string1[1].split('~', 1)
    searchval = string2[0]
    searchparam = string2[1]

    if (searchparam == 'Key'):

        if(searchval == 'C'):
            searchval = 0
        elif(searchval == 'C♯/D♭'):
            searchval = 1
        elif(searchval == 'D'):
            searchval = 2
        elif(searchval == 'D♯/E♭'):
            searchval = 3
        elif(searchval == 'E'):
            searchval = 4
        elif(searchval == 'F'):
            searchval = 5
        elif(searchval == 'F♯/G♭'):
            searchval = 6
        elif(searchval == 'G'):
            searchval = 7
        elif(searchval == 'G♯/A♭'):
            searchval = 8
        elif(searchval == 'A'):
            searchval = 9
        elif(searchval == 'A♯/B♭'):
            searchval = 10
        elif(searchval == 'B'):
            searchval = 11
        else:
            searchval = 'error'

    elif (searchparam == 'Time Signature'):
        searchval = searchval.split('/', 1)[0]
    elif (searchparam == 'Tempo'):
        searchval = searchval.split(' ', 1)[0]
    elif (searchparam == 'Loudness'):
        test = searchval.split('%', 1)[0]
        searchval = eval(test)/10. - 10
    else:
        searchval = eval(searchval.split('%', 1)[0])/100.


    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    chatter = Chatters.objects.get(name = str(request.user.username))
    auth_token = chatter.spotify_auth

    kwarg = 'target_' + searchparam
    sp = spotipy.Spotify(auth_token)

    if (searchparam == "Acousticness"):
        results = sp.recommendations(seed_tracks = [uri], target_acousticness = [searchval])
    elif (searchparam == "Danceability"):
        results = sp.recommendations(seed_tracks = [uri], target_danceability = [searchval])
    elif (searchparam == "Energy"):
        results = sp.recommendations(seed_tracks = [uri], target_energy = [searchval])
    elif (searchparam == "Instrumentalness"):
        results = sp.recommendations(seed_tracks = [uri], target_instrumentalness = [searchval])
    elif (searchparam == "Key"):
        results = sp.recommendations(seed_tracks = [uri], target_key = [searchval])
    elif (searchparam == "Liveness"):
        results = sp.recommendations(seed_tracks = [uri], target_liveness = [searchval])
    elif (searchparam == "Loudness"):
        results = sp.recommendations(seed_tracks = [uri], target_loudness = [searchval])
    elif (searchparam == "Speechiness"):
        results = sp.recommendations(seed_tracks = [uri], target_speechiness = [searchval])
    elif (searchparam == "Tempo"):
        results = sp.recommendations(seed_tracks = [uri], target_tempo = [searchval])
    elif (searchparam == "Time Signature"):
        results = sp.recommendations(seed_tracks = [uri], target_time_signature = [searchval])
    elif (searchparam == "Valence"):
        results = sp.recommendations(seed_tracks = [uri], target_valence = [searchval])
    else:
        results = 'Error'
    
    # print json.dumps(results, indent=6, sort_keys=True) # Pretty Print

    for track in results['tracks'][:20]:

        if (len(track['album']['images']) > 0):
            imagelink = track['album']['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_search = SearchRes(track=track['name'],
                               user = request.user,
                               artist=track['artists'][0]['name'],
                               album=track['album']['name'],
                               img=imagelink,
                               created=timezone.now(),
                               popularity = track['popularity'],
                               uri=track['uri']
                               )
        new_search.save()
        features = sp.audio_features(str(track['uri'].split(':')[2]))
        new_search.acousticness = features[0]['acousticness']
        new_search.danceability = features[0]['danceability']
        new_search.energy = features[0]['energy']
        new_search.instrumentalness = features[0]['instrumentalness']
        new_search.key = features[0]['key']
        new_search.liveness = features[0]['liveness']
        new_search.loudness = features[0]['loudness']
        new_search.speechiness = features[0]['speechiness']
        new_search.tempo = features[0]['tempo']
        new_search.time_signature = features[0]['time_signature']
        new_search.valence = features[0]['valence']
        new_search.save()

    response_text = serializers.serialize('json', SearchRes.objects.all())
    return HttpResponse(response_text, content_type='application/json')

# Get the first 20 tracks in a playlist
def get_playlist(request):

    if not 'item' in request.POST or not request.POST['item']:
        message = 'Playlist must have a URI to pass to the Spotify API.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    stringout = str(request.POST['item'])
    uri = stringout.split(':')[4]
    userid = stringout.split(':')[2]

    # print("Get Playlist")
    # print("URI:")
    # print(uri)
    # print("User ID:")
    # print(userid)

    # Delete previous search objects
    SearchRes.objects.filter(user = request.user).delete()
    ArtistRes.objects.filter(user = request.user).delete()
    GenreRes.objects.filter(user = request.user).delete()
    PlaylistRes.objects.filter(user = request.user).delete()

    chatter = Chatters.objects.get(name = str(request.user.username))
    auth_token = chatter.spotify_auth

    spotify = spotipy.Spotify(auth=auth_token)
    results = spotify.user_playlist(userid, uri)

    # print json.dumps(results, indent=6, sort_keys=True) # Pretty Print

    for track in results['tracks']['items'][:20]:

        if (len(track['track']['album']['images']) > 0):
            imagelink = track['track']['album']['images'][0]['url']
        else:
            imagelink = '../../static/img/egg.png'

        new_search = SearchRes(track=track['track']['name'],
                               artist=track['track']['artists'][0]['name'],
                               album=track['track']['album']['name'],
                               img=imagelink,
                               created=timezone.now(),
                               popularity = track['track']['popularity'],
                               uri=track['track']['uri'],
                               user = request.user
                               )
        new_search.save()

    response_text = serializers.serialize('json', SearchRes.objects.all())
    return HttpResponse(response_text, content_type='application/json')


def get_track_info(self, tid):

    start = time.time()
    features = sp.audio_features(tid)
    delta = time.time() - start
    for feature in features:
        print(json.dumps(feature, indent=4))
        print()
        analysis = sp._get(feature['analysis_url'])
        print(json.dumps(analysis, indent=4))
        print()
    print ("features retrieved in %.2f seconds" % (delta,))




