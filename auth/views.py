from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def password_changed(request):
    messages.add_message(request, messages.INFO, 'password_changed succussfully')
    return redirect(reverse('profile:home'))
