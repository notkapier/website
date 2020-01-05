from django.urls import path

from . import views

urlpatterns = [
		path('',views.index, name='index'),
		path('academics',views.academics, name='academics'),
		path('alumni',views.alumni, name='alumni'),
		path('digitallibrary',views.digitallibrary, name='digitallibrary'),
		path('traccer',views.traccer, name='traccer'),
		path('post/<int:post_id>',views.post, name='post'),
	]