from django.shortcuts import render
from django.views import View
from about.models import About
from social.models import Link
from portfolio.models import Portfolio
from projects.models import Post
from contact.models import Contact
from education.models import Education
from events_list.models import Event
from idiomas.models import Languague

class HomeView(View):
    def get(self, request):
        about = About.objects.all()
        social = Link.objects.all()
        portfolio = Portfolio.objects.first()
        projects = Post.objects.all()
        contact = Contact.objects.all()
        education = Education.objects.all()
        events = Event.objects.all()
        languague = Languague.objects.all()
        return render(request, "core/index.html", {'about': about,
                                                   'social': social,
                                                   'portfolio': portfolio,
                                                   'projects': projects,
                                                   'contact': contact,
                                                   'education': education,
                                                   'events': events,
                                                   'languague': languague
                                                   })


class HeaderView(View):
    def get(self, request):
        about = About.objects.all()
        social = Link.objects.all()
        portfolio = Portfolio.objects.first()
        projects = Post.objects.all()
        languague = Languague.objects.all()
        return render(request, "core/header.html", {'about': about,
                                                    'social': social,
                                                    'portfolio': portfolio,
                                                    'projects': projects,
                                                    'languague': languague
                                                    })