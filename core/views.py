from django.shortcuts import render, HttpResponse
from about.models import About
from social.models import Link


# Create your views here.
def home(request):
    about = About.objects.all()
    social = Link.objects.all()
    return render(request, "core/index.html", {'about': about,
                                               'social': social})
