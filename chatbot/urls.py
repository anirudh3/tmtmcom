from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from chatbot import views


urlpatterns = [
    # Route for the home page.
    url(r'^$', views.home),
    url(r'^home$', views.home, name='home'),

    # Route for built-in authentication with our own custom login page.
    url(r'^login$', auth_views.login, {'template_name':'chatbot/login.html'}, name='login'),

    # Route for adding a greeting message, then loggin in.
    url(r'^login-step$', views.login_step, name="login-step"),

    # Route for logging out the user
    url(r'^logout$', auth_views.logout_then_login, name='logout'),

    # Route for deleting all messages, then logging out
    url(r'^logout-step$', views.logout_step, name='logout-step'),

    # Route to send user to a registration page
    url(r'^register$', views.register, name='register'),

    # Route for the page saying an email has been sent to confirm email after registration
    url(r'^needs-confirmation$', views.needs_confirmation, name='needs-confirmation'),

    # Route to send user to the chat page
    url(r'^chat$', views.chat, name='chat'),

    # Route to send user to the explore page
    url(r'^explore$', views.explore, name='explore'),

    # Route to send user to the observe page
    url(r'^observe$', views.observe, name='observe'),

    # Route to send user to the you page
    url(r'^you$', views.you, name='you'),

    # Route to send user to the settings page
    url(r'^settings$', views.settings, name='settings'),

    # any token produced by the default_token_generator
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', views.confirm_registration, name='confirm'),

    # Route to edit a user's profile
    url(r'^edit-profile$', views.edit, name='edit'),

    # Route to upload an image
    url(r'^edit-pic/(?P<user_id>\w+)/$', views.upload_pic, name="uploadpic"),

    # Route to messaging to chatbot
    url(r'^add-chat$', views.add_chat),

    # Route to search with explore
    url(r'^add-explore$', views.add_explore),

    # Route to top ten artists
    url(r'^artist-top-ten$', views.artist_top_ten),

    # Route to tracks in a playlist
    url(r'^get-playlist$', views.get_playlist),

    # Route to get genre search results
    url(r'^search-genre$', views.search_artist_with_genre),

    # Route to respond by chatbot
    url(r'^respond-chat$', views.respond_chat),

    # Route to add the Spotify token to the user's model
    url(r'^add-spotify-token$', views.add_spotify_token),

    # Route to returning a spotify login
    url(r'^callback$', views.spotify_callback),
    
    # JQuery URLS
    url(r'^get-list-json$', views.get_list_json, name='getlistjson'),
    url(r'^get-explore-json$', views.get_explore_json, name='getexplorejson'),
    url(r'^get-list-xml$', views.get_list_xml, name='getlistxml'),
    url(r'^get-list-xml-template$', views.get_list_xml_template, name='getlistxmltemp'),

]
