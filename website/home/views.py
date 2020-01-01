from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Post,Element,PostStatus,Announcement,Course,Batch
from django.utils.html import escape

# Create your views here.
def index(request):
	feature = PostStatus.objects.get(post_status='Featured')
	# posts = Post.objects.order_by('-pub_date').get[:6]
	try:
		posts = Post.objects.order_by('-pub_date')[:6]
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

