from django.urls import path

from . import views

urlpatterns = [
		path('',views.index, name='index'),
		path('academics',views.academics, name='academics'),
		path('alumni',views.alumni, name='alumni'),
	]