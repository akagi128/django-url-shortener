from xxlimited import new

from django.shortcuts import render , redirect
from django.http import *
from .models import ShortURL
# Create your views here.
import secrets
import string

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def home(req):
    shortcode = req.GET.get("shortcode")
    shorturl = f"https://short.ly/{shortcode}" if shortcode else None
    return render(req, "shorter/index.html", {
            "shorturl": shorturl
        })

def shorten(req):
    url = req.POST.get("url")

    exist = ShortURL.objects.filter(origUrl = url).first()

    if exist:
        shortcode = exist.shortcode
    else:
       shortcode = generate_short_code()
       new_url = ShortURL(origUrl = url , shortcode = shortcode )
       new_url.save()

    #shorturl = req.build_absolute_uri(f"/{shortcode}/")

    return redirect(f"/?shortcode={shortcode}")
