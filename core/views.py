from django.shortcuts import render, HttpResponse
from about.models import About
from social.models import Link
from portfolio.models import Portfolio


# Create your views here.
def home(request):
    about = About.objects.all()
    social = Link.objects.all()
    portfolio = Portfolio.objects.first()
    return render(request, "core/index.html", {'about': about,
                                               'social': social,
                                               'portfolio': portfolio})
