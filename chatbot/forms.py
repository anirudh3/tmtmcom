from django import forms

from django.contrib.auth.models import User
from models import *

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control my-1'}))
    last_name  = forms.CharField(max_length=20, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control my-1'}))
    email      = forms.CharField(max_length=50, label='',
                                 widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control my-1'}))
    location = forms.ChoiceField(choices = locations, label='',
                                 widget = forms.Select(attrs={'placeholder': 'Location', 'class': 'form-control my-1'}))
    username   = forms.CharField(max_length = 20, label='',
                                 widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control my-1'}))
    password1  = forms.CharField(max_length = 200, label='', 
                                 widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control my-1'}))
    password2  = forms.CharField(max_length = 200, label='',  
                                 widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control my-1'}))


    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(RegistrationForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # Get the right code for the location
        loc = cleaned_data.get('location')

        bigdict = dict(locations)
        outl = ''

        for l in bigdict:
            if (loc == bigdict[str(l)]):
                outl = l

        # We must return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username

    class Meta:
        model = User
        labels = {
        }

# class FollowForm(forms.ModelForm):
#     # Customizes form validation for the username field.
#     def clean_followers(self):
#         # Confirms that the username is not already present in the
#         # User model database.
#         username = self.cleaned_data.get('username')
#         if User.objects.filter(username__exact=username):
#             raise forms.ValidationError("Username is already taken.")

#         # We must return the cleaned data we got from the cleaned_data
#         # dictionary
#         return username

#     class Meta:
#         model = Posters
#         fields = ['following']


class AddForm(forms.ModelForm):
    item = forms.CharField(max_length=160, label='', widget=forms.TextInput(attrs={'placeholder': 'Thoughts', 'class': 'form-control my-0', 'aria-describedby': 'sizing-addon1'}))

    def clean(self):
        cleaned_data = super(AddForm, self).clean()

        text = cleaned_data.get('mess')
        if len(text) > 160:
            raise forms.ValidationError("Post is longer that 160 characters.")

        return cleaned_data

    class Meta:
        model = Mess
        fields = ['item']
        exclude = ['text']

# class AddComment(forms.ModelForm):
#     comment = forms.CharField(max_length=160, label='', widget=forms.TextInput(attrs={'placeholder': 'Comments', 'class': 'form-control my-0', 'aria-describedby': 'sizing-addon1'}))

#     def clean(self):
#         cleaned_data = super(AddComment, self).clean()

#         text = cleaned_data.get('comment')
#         if len(text) > 160:
#             raise forms.ValidationError("Comment is longer than 160 characters.")

#         return cleaned_data

#     class Meta:
#         model = Comment
#         fields = ['comment']
#         exclude = ['text']

class EditForm(forms.ModelForm):

    first_name = forms.CharField(max_length=20, label='', required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control my-1', 'id': 'f-firstname'}))
    last_name  = forms.CharField(max_length=20, label='',required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control my-1', 'id': 'f-lastname'}))
    age = forms.CharField(max_length=20, label='', required=False,
                          widget=forms.TextInput(attrs={'placeholder': 'Age', 'class': 'form-control my-1', 'id': 'f-age'}))
    email      = forms.CharField(max_length=50, label='',required=False,
                                 widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control my-1', 'id': 'f-email'}))
    location = forms.ChoiceField(choices = locations, label='',required=False,
                                 widget = forms.Select(attrs={'placeholder': 'Location', 'class': 'form-control my-1', 'id': 'f-location'}))

    def clean(self):
        cleaned_data = super(EditForm, self).clean()

        age = cleaned_data.get('age')
        if len(age) > 5:
            raise forms.ValidationError("Age is too old. Enter feasable age.")

        # Get the right code for the location
        loc = cleaned_data.get('location')

        bigdict = dict(locations)
        outl = ''

        for l in bigdict:
            if (loc == bigdict[str(l)]):
                outl = l

        return cleaned_data


    class Meta:
        model = Chatters
        fields = (
            'first_name',
        )

# class UploadImageForm(forms.Form):
#     image = forms.ImageField()

#     def clean(self):
#         cleaned_data = super(UploadImageForm, self).clean()

#         return cleaned_data


