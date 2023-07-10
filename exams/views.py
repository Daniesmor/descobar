from django.shortcuts import render, HttpResponse
from about.models import About
from social.models import Link
from portfolio.models import Portfolio
from projects.models import Post
from contact.models import Contact
from education.models import Education
from events_list.models import Event


# Create your views here.
def exams(request):
    about = About.objects.all()
    social = Link.objects.all()
    portfolio = Portfolio.objects.first()
    projects = Post.objects.all()
    contact = Contact.objects.all()
    education = Education.objects.all()
    events = Event.objects.all()
    return render(request, "exams/index.html", {'about': about,
                                               'social': social,
                                               'portfolio': portfolio,
                                               'projects': projects,
                                               'contact': contact,
                                               'education': education,
                                               'events': events})
