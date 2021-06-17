from django.shortcuts import redirect, render, HttpResponse
import uuid
from .models import URL

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        print(uid)
        new_url = URL(link = url, shortUrl = uid)
        new_url.save()
       
        return HttpResponse(uid)

def direct(request, pk):
    url_details = URL.objects.get(shortUrl = pk)
    print(url_details)
    return redirect('https://'+url_details.link)
