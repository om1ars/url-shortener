from django.shortcuts import render
import uuid
from .models import Url


def index(req):
    return render(req, "index.html")


def create(req):
    if req.method == "POST":
        link = req.POST['link']
        uuid