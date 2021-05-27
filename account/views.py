from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'login.html',)
