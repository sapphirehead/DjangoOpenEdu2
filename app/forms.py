"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Пароль"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Your name', min_length=2, max_length=100)
    city = forms.CharField(label='Your city', min_length=2, max_length=100)
    job = forms.CharField(label='Your job ', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Your gender', 
                               choices=[('1', 'Man'), ('2', 'Woman')],
                               widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Do you using internet?', 
                               choices=(('1', 'Every day'), 
                                        ('2', 'Few times in each day'),
                                        ('3', 'Few times in each week'),
                               ('4', 'Few times in each month')), initial=1)
    notice = forms.BooleanField(label='Do you want site-news on your e-mail?',
                                required=False)
    email = forms.EmailField(label='Your e-mail', min_length=7)
    message = forms.CharField(label='Tell us about yourself',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:    
        model = Comment # используемая модель        
        fields = ('text',) # требуется заполнить только поле text        
        labels = {'text': "Comment"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:    
        model = Blog # используемая модель        
        fields = ('title', 'descriptions', 'content', 'posted', 'author',
                 'image',) # it required contents all this fields       
        labels = {'title': "Title", 'description': 'Short describe',
                  'content': 'Summary', 'posted': 'Date', 
                  'author': 'Author', 'image': 'Image'} # метка к полю формы text
