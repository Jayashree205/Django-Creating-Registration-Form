from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Pass the username to the template
            return render(request, 'success.html', {'username': user.username})
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})
