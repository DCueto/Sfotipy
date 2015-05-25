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


from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponse

class LoginView(TemplateView):
	template_name = "login.html"

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		is_auth = False
		name = None

		if self.request.user.is_authenticated():
			is_auth = True
			name = self.request.user.username

		data = {
		'is_auth': is_auth,
		'name': name,
		}

		context.update(data)
		return context


class ProfileView(TemplateView):
	template_name = 'profile.html'

	def get_userprofile(self):
		return self.request.user.userprofile

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)

		if self.request.user.is_authenticated():
			context.update({'userprofile': self.get_userprofile()})

		return context


class PerfilRedirectView(RedirectView):
	pattern_name = 'profile'








