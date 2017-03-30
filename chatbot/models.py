from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

# Data Model for additional user information
class Chatters(models.Model):
    username = models.OneToOneField(User, related_name="one2one_user", blank=True, null=True)
    name = models.CharField(max_length=160, blank=True)
    age = models.CharField(max_length=5, blank=True)
    image = models.ImageField(upload_to='static/img/', default='/static/img/egg.jpg')
    spotify = models.CharField(max_length=430, blank=True)

    def __unicode__(self):
        return 'Entry(id=' + str(self.id) + ')'

# Data model for a chat message
class Mess(models.Model):
    text = models.CharField(max_length=160)
    user = models.ForeignKey(User, default=None)
    created = models.DateTimeField(default=None)

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.text + '"'

    class Meta:
    	ordering = ["-created"]