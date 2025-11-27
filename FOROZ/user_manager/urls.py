from . import views
from django.urls import path

urlpatterns = [
	path('register', views.register, name='Registration'),
	path('signup', views.signup, name="Registration-Form"),
	path('login', views.login, name="Login-Page")
]