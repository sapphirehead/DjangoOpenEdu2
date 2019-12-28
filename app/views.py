"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import AnketaForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария
from .forms import BlogForm # использование формы ввода новой статьи
from django.contrib import admin
#admin.autodiscover()

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Домашняя страница',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Мои реквизиты.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Информация',
            'message':'Главная',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Ссылки',
            'message':'Полезные ресурсы.',
            'year':datetime.now().year,
        }
    )

def questionnarie(request):
    """Renders the Anketa page."""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Man', '2': 'Woman'}
    internet = {'1': 'Every day', '2': 'Few times in each day',
                '3': 'Few times in each week', '4': 'Few times in each month'}
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data['gender']]
            data['internet'] = internet[form.cleaned_data['internet']]
            if form.cleaned_data['notice'] == True:
                data['notice'] = 'Yes'
            else:
                data['notice'] = 'No'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/questionnarie.html',
        {
            'title': 'Анкета',
            'form': form,
            'data': data, # with this throwing Exception
            'year':datetime.now().year,
        }
    )
def registration(request):
    """Renders the registration page."""    
    if request.method == "POST": # после отправки формы    
        regform = UserCreationForm (request.POST)    
        if regform.is_valid(): #валидация полей формы    
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы    
            reg_f.is_staff = False # запрещен вход в административный раздел        
            reg_f.is_active = True # активный пользователь        
            reg_f.is_superuser = False # не является суперпользователем        
            reg_f.date_joined = datetime.now() # дата регистрации        
            reg_f.last_login = datetime.now() # дата последней авторизации        
            reg_f.save() # сохраняем изменения после добавления данных        
            return redirect('home') # переадресация на главную страницу после регистрации    
    else:    
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя        
        assert isinstance(request, HttpRequest)        
    return render(        
        request,        
        'app/registration.html',        
        {        
            'title': 'Регистрация пользователя',
            'regform': regform, # передача формы в шаблон веб-страницы            
            'year':datetime.now().year,    
        }    
    )

def blog(request):
    """Renders the blog page."""    
    assert isinstance(request, HttpRequest)    
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели    
    return render(        
        request,        
        'app/blog.html',        
        {        
            'title': 'Блог',        
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year': datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""    
    assert isinstance(request, HttpRequest)    
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)        
        if form.is_valid():        
            comment_f = form.save(commit=False)            
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя            
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату            
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий            
            comment_f.save() # сохраняем изменения после добавления полей        
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария        
    else:        
        form = CommentForm() # создание формы для ввода комментария
    return render(    
        request,        
        'app/blogpost.html',        
        {        
            'title': post_1.title,
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы добавления комментария в шаблон веб-страницы 
            'year': datetime.now().year,  # with this string it's throwing exceptions    
        }    
    )

def newpost(request):
    """Renders the newpost page."""
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        #blog = Blog.objects.filter(post)
        blogform =  BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit = False)
            blog_f.posted = datetime.now()
            blog_f.save() # saving the changing after added article
            return redirect('blog') # redirect on blog's page after saving
    else:
        blogform = BlogForm() # creating object of form for data inputing
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {
            'title': 'Добавить статью',
            'blogform': blogform, # putting form to web-page's template
            'year': datetime.now().year,# with this throwing exception
        }
    )
def videopost(request):
    """Renders the video-page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Video',
            'message':'Video-clip', # with this throwing exception
            'year':datetime.now().year,# with this throwing exception
        }
    )