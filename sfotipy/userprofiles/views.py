# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from .forms import UserCreationEmailForm, EmailAuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

		#loguear al usuario
		email = request.POST.get('email') #email del formulario
		password = request.POST.get('password2') #contraseña del formulario
		user = authenticate(email=email, password=password) #objeto del usuario creado en el formulario
		login(request, user)

		#crear userprofile
		#redireccinar al home
		return redirect('home')

	return render(request, 'signup.html', {'form': form})

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())

		#redireccionar al home
		return redirect('home')


	return render(request, 'signin.html', {'form' : form})

def signout(request):
	logout(request)
	bye = "You're logged out"

	return render(request, 'signout.html', {'bye' : bye})


