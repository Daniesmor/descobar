from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from about.models import About
from social.models import Link
from portfolio.models import Portfolio
from projects.models import Post


def projects(request, post_title):
    posts = get_object_or_404(Post, title=post_title)
    about = About.objects.all()
    social = Link.objects.all()
    portfolio = Portfolio.objects.first()
    projects = Post.objects.all()
    return render(request, "projects/projects.html", {'posts': posts,
                                                      'about': about,
                                                      'social': social,
                                                      'portfolio': portfolio,
                                                      'projects': projects})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "projects/category.html", {'category': category})
