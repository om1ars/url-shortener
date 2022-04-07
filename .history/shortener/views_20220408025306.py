from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse



def index(req):
    return render(req, "index.html")


def create(req):
    if req.method == "POST":
        link = req.POST['link']
        uid = str(uuid.uuid4()[:5])
        new_url = Url(link=link, uuid=uid)
        new_url.json()


        return HttResponse(uid)

def go(req, pk):
    url_details = Url.objects.get(uuid=pk)

    return redirect("https://")