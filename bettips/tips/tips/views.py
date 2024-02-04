from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tip, Category, UserProfile
from .forms import TipForm, UserRegistrationForm


def tip_list(request):
    tips = Tip.objects.all()
    return render(request, 'tips/tip_list.html', {'tips': tips})


#To login

def submit_tip(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            return redirect('tip_list')
    else:
        form = TipForm()
    return render(request, 'tips/submit_tip.html', {'form': form})

#login required
def user_profile(request):
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    return render(request, 'tips/user_profile.html', {'profile' : profile})

def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user)
            profile.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})












