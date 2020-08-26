from django.views.generic.edit import CreateView
from .models import SiteUser
from .forms import SiteUserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ssusers.models import Account, Character, Inventoryitem

class SiteUserCreation(CreateView):
    model = SiteUser
    form_class = SiteUserCreationForm
    success_url = reverse_lazy('login')

def index(request):
    return render(request, 'siteusers/home.html', {'title':'Home'})

@login_required
def download(request):
    return render(request, 'siteusers/download.html', {'title':'Download'})

def donate(request):
    return render(request, 'siteusers/donate.html', {'title':'Donate'})

@login_required
def profile(request):
    username=request.user.username
    accounts=Account.objects.all()
    account=accounts.get(name=username)
    characters = Character.objects.filter(accountid=account.id)

    online_users=accounts.filter(loggedin__gt=0)

    return render(request, 'siteusers/profile.html',
                    {
                    'title':'Profile',
                    'characters':characters,
                    'accounts':accounts,
                    'online_users':online_users,

                    }
                )
