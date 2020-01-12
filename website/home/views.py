from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Post,Element,PostStatus,Announcement,Course,Batch,Library,Reference,Traccer,TraccerItem,AboutTab
from django.utils.html import escape
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
import os
from django.conf import settings


# Create your views here.
def index(request):
	feature = PostStatus.objects.get(post_status='Featured')
	# posts = Post.objects.order_by('-pub_date').get[:6]
	try:
		posts = Post.objects.filter(status_id=PostStatus.objects.get(post_status='Active')).order_by('-pub_date')[:6]
	except Post.DoesNotExist:
		posts = None
	try:
		featured = Post.objects.get(status_id=feature.id)
	except Post.DoesNotExist:
		featured = Post(post_title='sample featured post',post_description='Sample Featured Description Sample Featured Description Sample Featured Description Sample Featured Description',post_image='/uploads/home.jpg',status_id=feature.id)
	e = Element()
	banner = e.getbanner()
	logo = e.getlogo()

	try:
		announcements = Announcement.objects.order_by('-pub_date')[:5]
	except Announcement.DoesNotExist:
		announcements = None
	# output = ', '.join([p.post_title for p in posts])
	return render(request,'home/index.html',{'posts':posts,'banner':banner,'logo':logo,'featured':featured,'announcements':announcements})

def academics(request):
	e = Element()
	banner = e.getbanner()
	logo = e.getlogo()
	c = Course()
	courses = c.getAllCourses()
	return render(request,'home/academics.html',{'courses':courses,'banner':banner,'logo':logo})

def alumni(request):
	c = Course()
	b = Batch()
	e = Element()
	logo = e.getlogo()
	courses = c.getAllCourses()
	batches = b.getAllBatches()
	return render(request,'home/alumni.html',{'courses':courses,'batches':batches,'logo':logo})	

@csrf_exempt
def digitallibrary(request,library_id=0):
	e = Element()
	logo = e.getlogo()
	l = Library()
	libraries = l.getAllLibraries()
	if request.is_ajax():
		library_id = request.POST['library_id']
		library_name = Library.objects.get(id=library_id).library_name
		# r = Reference()
		references = Reference.objects.filter(library_id=library_id)
		# return render('home/sample.html',{'references':r.getAllReference(library_id)})
		return render(request, "home/reference.html", {'references':references,'library_name':library_name})
		# html = render_to_string('home/sample.html',{'references':references})
		# return HttpResponse(html)
	else:
		if libraries is None:
			return render(request,'home/digitallibrary.html',{'libraries':None,'references':None,'logo':logo})
		else:
			if library_id==0:
				library = Library.objects.first()
			else:
				library = Library.objects.get(id=library_id)
			if library is None:
				return render(request,'home/digitallibrary.html',{'libraries':None,'references':None,'logo':logo})
			else:
				library_id = library.id
				library_name = library.library_name
				references = Reference.objects.filter(library_id=library_id)
				return render(request,'home/digitallibrary.html',{'libraries':libraries,'references':references,'library_name':library_name,'logo':logo})
@csrf_exempt
def traccer(request,traccer_id=0):
	e = Element()
	logo = e.getlogo()
	t = Traccer()
	traccers = t.getAllTraccers()
	if request.is_ajax():
		traccer_id = request.POST['traccer_id']
		# r = Reference()
		traccer_type = Traccer.objects.get(id=traccer_id).traccer_type
		tracceritems = TraccerItem.objects.filter(traccer_id=traccer_id)
		# return render('home/sample.html',{'references':r.getAllReference(library_id)})
		return render(request, "home/tracceritems.html", {'tracceritems':tracceritems,'traccer_type':traccer_type})
		# html = render_to_string('home/sample.html',{'references':references})
		# return HttpResponse(html)
	else:
		if traccers is None:
			return render(request,'home/traccer.html',{'tracceritems':None,'tracceritems':None,'logo':logo})
		else:
			if traccer_id == 0:
				traccer = Traccer.objects.first()
			else:
				traccer = Traccer.objects.get(id=traccer_id)	
			if traccers is None:
				return render(request,'home/traccer.html',{'tracceritems':None,'tracceritems':None,'logo':logo})
			else:
				traccer_id = traccer.id
				traccer_type = traccer.traccer_type
				tracceritems = TraccerItem.objects.filter(traccer_id=traccer_id)
				return render(request,'home/traccer.html',{'traccers':traccers,'tracceritems':tracceritems,'logo':logo,'traccer_type':traccer_type})
def post(request,id):
	post = Post.objects.get(id=id)
	# posts = Post.objects.order_by('-pub_date').get[:6]
	e = Element()
	banner = e.getbanner()
	logo = e.getlogo()

	try:
		announcements = Announcement.objects.order_by('-pub_date')[:5]
	except Announcement.DoesNotExist:
		announcements = None
	return render(request,'home/post.html',{'banner':banner,'logo':logo,'post':post,'announcements':announcements})

def reference(request,id):
	reference = Reference.objects.get(id=id)
	# posts = Post.objects.order_by('-pub_date').get[:6]

	e = Element()
	banner = e.getbanner()
	logo = e.getlogo()

	library = Library.objects.get(id=reference.library_id)

	return render(request,'home/referenceitem.html',{'banner':banner,'logo':logo,'reference':reference,'library':library})			

def download(request, id):
	path = Reference.objects.get(id = id).filename
	file_path = os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type = "application/octet-stream")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404

def download_announcement(request, id):
	path = Announcement.objects.get(id = id).filename
	file_path = os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type = "application/octet-stream")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404
def download_tracceritem(request, id):
	path = Announcement.objects.get(id = id).filename
	file_path = os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type = "application/octet-stream")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404
def tracceritem(request,id):
	tracceritem = TraccerItem.objects.get(id=id)
	e = Element()
	banner = e.getbanner()
	logo = e.getlogo()
	traccer = Traccer.objects.get(id=tracceritem.traccer_id)
	return render(request,'home/tracceritem.html',{'banner':banner,'logo':logo,'tracceritem':tracceritem,'traccer':traccer})
@csrf_exempt
def aboutus(request,id=0):
	e = Element()
	logo = e.getlogo()
	a = AboutTab()
	abouttabs = a.getAllAboutTabs()
	if request.is_ajax():
		id = request.POST['id']
		# r = Reference()
		abouttab = AboutTab.objects.get(id=id)
		return render(request, "home/aboutusitems.html", {'abouttabs':abouttabs,'abouttab':abouttab})
		# html = render_to_string('home/sample.html',{'references':references})
		# return HttpResponse(html)
	else:
		if abouttabs is None:
			return render(request,'home/aboutus.html',{'abouttabs':None,'abouttab':None,'logo':logo})
		else:
			if id == 0:
				abouttab = AboutTab.objects.first()
			else:
				abouttab = AboutTab.objects.get(id=id)	
			if abouttabs is None:
				return render(request,'home/aboutus.html',{'abouttabs':None,'abouttab':None,'logo':logo})
			else:
				return render(request,'home/aboutus.html',{'abouttabs':abouttabs,'abouttab':abouttab,'logo':logo})