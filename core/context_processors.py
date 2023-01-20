from datetime import datetime
from django.conf import settings  # this is a good example of extra
from about.models import About
from social.models import Link
from portfolio.models import Portfolio
from projects.models import Post


def default(request):
    about = About.objects.all()
    social = Link.objects.all()
    portfolio = Portfolio.objects.first()
    projects = Post.objects.all()
    # them as a dictionary to be added to each template's context:
    return {'about': about,
            'social': social,
            'portfolio': portfolio,
            'projects': projects}
