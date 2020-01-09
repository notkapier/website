from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Post,Element,PostStatus,Announcement,Course,Batch,Library,Reference,Traccer,TraccerItem
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
	courses = c.getAllCourses()
	batches = b.getAllBatches()
	return render(request,'home/alumni.html',{'courses':courses,'batches':batches})	

@csrf_exempt
def digitallibrary(request,library_id=0):
	l = Library()
	libraries = l.getAllLibraries()
	if request.is_ajax():
		library_id = request.POST['library_id']
		# r = Reference()
		references = Reference.objects.filter(library_id=library_id)
		# return render('home/sample.html',{'references':r.getAllReference(library_id)})
		return render(request, "home/reference.html", {'references':references})
		# html = render_to_string('home/sample.html',{'references':references})
		# return HttpResponse(html)
	else:
		if libraries is None:
			return render(request,'home/digitallibrary.html',{'libraries':None,'references':None})
		else:
			library = Library.objects.first()
			if library is None:
				return render(request,'home/digitallibrary.html',{'libraries':None,'references':None})
			else:
				library_id = library.id
				references = Reference.objects.filter(library_id=library_id)
				return render(request,'home/digitallibrary.html',{'libraries':libraries,'references':references})
@csrf_exempt
def traccer(request,traccer_id=0):
	t = Traccer()
	traccers = t.getAllTraccers()
	if request.is_ajax():
		traccer_id = request.POST['traccer_id']
		# r = Reference()
		tracceritems = TraccerItem.objects.filter(traccer_id=traccer_id)
		# return render('home/sample.html',{'references':r.getAllReference(library_id)})
		return render(request, "home/tracceritem.html", {'tracceritems':tracceritems})
		# html = render_to_string('home/sample.html',{'references':references})
		# return HttpResponse(html)
	else:
		if traccers is None:
			return render(request,'home/traccer.html',{'tracceritems':None,'tracceritems':None})
		else:
			traccer = Traccer.objects.first()
			if traccers is None:
				return render(request,'home/traccer.html',{'tracceritems':None,'tracceritems':None})
			else:
				traccer_id = traccer.id
				tracceritems = TraccerItem.objects.filter(traccer_id=traccer_id)
				return render(request,'home/traccer.html',{'traccers':traccers,'tracceritems':tracceritems})
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