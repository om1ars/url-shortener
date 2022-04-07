from django.shortcuts import render
import uuid
from .models import Url


def index(req):
    return render(req, "index.html")


