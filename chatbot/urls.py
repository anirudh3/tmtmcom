from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from chatbot import views


urlpatterns = [
    # Route for the home page.
    url(r'^$', views.home),
    url(r'^home$', views.home, name='home'),

    # Route for built-in authentication with our own custom login page.
    url(r'^login$', auth_views.login, {'template_name':'chatbot/login.html'}, name='login'),

    # Route for logging out the user
    url(r'^logout$', auth_views.logout_then_login, name='logout'),

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

    # url(r'^add-item$', views.add_item, name='add-item'),
    # # Parses number from URL and uses it as the item_id argument to the action
    # url(r'^delete-item/(?P<item_id>\d+)$', views.delete_item, name='delete-item'),
    # # Route for built-in authentication with our own custom login page

    
    
    # # Route to view a user's posts
    # url(r'^profile/(?P<user_id>\w+)/$', views.profile, name='profile'),

    # # Route to view followed people
    # url(r'^follow$', views.follow, name='follow'),
    # # Route to add a follower
    # url(r'^follow/(?P<user_id>\w+)/$', views.addfollow, name='addfollow'),
    # # Route to del a follower
    # url(r'^unfollow/(?P<user_id>\w+)/$', views.unfollow, name='unfollow'),
    # # Route to adding a comment
    # url(r'^add-comment/(?P<post_id>\w+)/$', views.add_comment, name='add-comment'),
    # # JQuery URLS
    # url(r'^get-list-json$', views.get_list_json, name='getlistjson'),
    # url(r'^get-follow-list-json$', views.get_follow_list_json, name='getfollowlistjson'),
    # url(r'^get-list-xml$', views.get_list_xml, name='getlistxml'),
    # url(r'^get-list-xml-template$', views.get_list_xml_template, name='getlistxmltemp'),
    # # The following URL should match any username valid in Django and

]
