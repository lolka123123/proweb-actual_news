from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
import random

def index(request):
    articles = models.Article.objects.all()

    page = 1

    paginator = Paginator(articles, 26)


    context = {
        'title': 'Actual News',
        'categories': models.Category.objects.all(),
        'articles': paginator.page(page).object_list,
        'paginator_has_previous': paginator.page(page).has_previous(),
        'paginator_has_next': paginator.page(page).has_next(),
        'paginator_page_previous': page-1,
        'paginator_page_next': page+1,
        'paginator_page': page,
        'paginator': paginator,
        'category_sorted': False,
    }

    return render(request, 'news/index.html', context)

def index_pagination(request, page):
    articles = models.Article.objects.all()

    paginator = Paginator(articles, 26)



    context = {
        'title': 'Actual News',
        'categories': models.Category.objects.all(),
        'articles': paginator.page(page).object_list,
        'paginator_has_previous': paginator.page(page).has_previous(),
        'paginator_has_next': paginator.page(page).has_next(),
        'paginator_page_previous': page-1,
        'paginator_page_next': page+1,
        'paginator_page': page,
        'paginator': paginator,
        'category_sorted': False,
    }

    return render(request, 'news/index.html', context)



def category(request, pk):
    articles = models.Article.objects.filter(category_id=pk)

    page = 1

    paginator = Paginator(articles, 26)

    context = {
        'title': 'Actual News',
        'categories': models.Category.objects.all(),
        'articles': paginator.page(1).object_list,
        'paginator_has_previous': paginator.page(page).has_previous(),
        'paginator_has_next': paginator.page(page).has_next(),
        'paginator_page_previous': page-1,
        'paginator_page_next': page+1,
        'paginator_page': page,
        'paginator': paginator,
        'category_sorted': True,


    }
    return render(request, 'news/index.html', context)



def user_register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = forms.RegistrationForm()


    context = {
        'title': 'Регистрация',
        'categories': models.Category.objects.all(),
        'form': form,
    }
    return render(request, 'news/user_form.html', context)

def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('register')
    else:
        form = forms.LoginForm()

    context = {
        'title': 'Вход в аккаунт',
        'categories': models.Category.objects.all(),
        'request': request,
        'form': form,
    }
    return render(request, 'news/user_form.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')

def my_profile(request):
    if not request.user.is_authenticated:
        return redirect('index')

    profile = models.Profile.objects.get(user_id=request.user.id)

    try:
        profile_image = profile.image.url
    except:
        profile_image = 'none'

    context = {
        'title': 'Профиль',
        'categories': models.Category.objects.all(),
        'profile': profile,
        'profile_image': profile_image,
        'request': request,
    }
    return render(request, 'news/profile.html', context)

def article_view(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except:
        return redirect('index')

    comments = models.Comment.objects.filter(article=article)

    if request.user.is_authenticated:
        profile = models.Profile.objects.get(user=request.user)
        if request.method == 'POST':
            form = forms.AuthenticatedCommentForm(data=request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.name = profile.user.username
                comment.profile_id = profile.id
                comment.article = article

                comment.save()

                return redirect('article', pk)
            else:
                return redirect('article', pk)
        else:
            form = forms.AuthenticatedCommentForm()
    else:
        profile = None
        if request.method == 'POST':
            form = forms.UnauthenticatedCommentForm(data=request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.profile_id = 0
                comment.article = article

                comment.save()

                return redirect('article', pk)
            else:
                return redirect('article', pk)
        else:
            form = forms.UnauthenticatedCommentForm()

    if profile:
        profile_id = profile.id
    else:
        profile_id = None

    context = {
        'title': f'Страница: {article.title}',
        'request': request,
        'categories': models.Category.objects.all(),
        'article': article,
        'comments': comments,
        'form': form,
        'profile_id': profile_id,
    }
    return render(request, 'news/article.html', context)


def delete_comment(request, pk):
    try:
        comment = models.Comment.objects.get(id=pk)
        profile = models.Profile.objects.get(user=request.user)
        if comment.profile_id == profile.id:
            comment.delete()
            return redirect('article', comment.article.id)
        else:
            return redirect('index')
    except:
        return redirect('index')


def edit_profile(request):
    try:
        profile = models.Profile.objects.get(user=request.user)
    except:
        return redirect('index')
    if request.method == 'POST':
        form = forms.ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('my_profile')
    else:
        form = forms.ProfileEditForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'news/edit_profile.html', context)

