from django.shortcuts import render, redirect
import uuid
from .models import URL
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = URL(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def goto(request, pk):
    url_details = URL.objects.get(uuid = pk)
    return redirect(url_details.link)