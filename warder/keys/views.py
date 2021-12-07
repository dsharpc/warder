from django.shortcuts import render
from .models import Credential

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'keys/login_needed.html')
    creds = Credential.objects.order_by('site')

    return render(request, 'keys/home.html', {'creds': creds})