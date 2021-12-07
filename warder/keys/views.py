from django.shortcuts import render
from .models import Credential

# Create your views here.
def home(request):

    creds = Credential.objects.order_by('site')

    return render(request, 'keys/home.html', {'creds': creds})