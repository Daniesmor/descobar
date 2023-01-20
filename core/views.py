from django.shortcuts import render, HttpResponse
from about.models import About
from social.models import Link
from portfolio.models import Portfolio
from projects.models import Post
from contact.models import Contact
from education.models import Education

# Create your views here.
def home(request):
    about = About.objects.all()
    social = Link.objects.all()
    portfolio = Portfolio.objects.first()
    projects = Post.objects.all()
    contact = Contact.objects.all()
    education = Education.objects.all()
    return render(request, "core/index.html", {'about': about,
                                               'social': social,
                                               'portfolio': portfolio,
                                               'projects': projects,
                                               'contact': contact,
                                               'education': education})


def header(request):
    about = About.objects.all()
    social = Link.objects.all()
    portfolio = Portfolio.objects.first()
    projects = Post.objects.all()
    return render(request, "core/header.html", {'about': about,
                                               'social': social,
                                               'portfolio': portfolio,
                                               'projects': projects})
