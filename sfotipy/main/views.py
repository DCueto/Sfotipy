from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	hola = "Bienvenido a sfotipy"

	return render(request, 'home.html', {'hola' : hola})