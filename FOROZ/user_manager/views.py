from django.shortcuts import render, redirect
from django.contrib import messages
# from home.models import Photo
# from users.models import me
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage

def register(request):
	# return HttpResponse('This is Hello WOrld')
	return render(request, 'signup.html')
	# return redirect('/user/login')

def login(request):
	return render(request, 'login.html')

def signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		re_pass = request.POST['re_pass']

		if password == re_pass:
			user = User.objects.create_user(email=email, username=username, password=re_pass)
			user.save()
			keys = ['abbas', 'abbass', 'malikzada', 'abbassmalikzada']
			for i in keys:
				if username.lower() == i:
					messages.success(request, f'Welcome shekih !! - see the magic?')
				else:
					messages.success(request, f'Welcome {username} !!')
			return redirect('/user/login')
		else:
			return HttpResponse('error')