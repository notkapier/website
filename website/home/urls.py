from django.urls import path

from . import views

urlpatterns = [
		path('',views.index, name='index'),
		path('academics',views.academics, name='academics'),
		path('alumni',views.alumni, name='alumni'),
		path('digitallibrary',views.digitallibrary, name='digitallibrary'),
		path('digitallibrary/<int:library_id>/',views.digitallibrary, name='digitallibrary'),
		path('traccer',views.traccer, name='traccer'),
		path('traccer/<int:traccer_id>/',views.traccer, name='traccer'),
		path('post/<int:id>/',views.post, name='post'),
		path('reference/<int:id>/',views.reference, name='referenceitem'),
		path('download/<int:id>/',views.download, name='download'),
		path('download_announcement/<int:id>/',views.download_announcement, name='download_announcement'),
		path('tracceritem/<int:id>/',views.tracceritem, name='tracceritem'),
		path('download_tracceritem/<int:id>/',views.download_tracceritem, name='download_tracceritem'),
		path('aboutus',views.aboutus, name='aboutus'),
		path('aboutus/<int:id>/',views.aboutus, name='aboutus'),
		
	]