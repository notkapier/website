from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-pub_date')[:6]
	output = ', '.join([p.post_title for p in posts])
	return render(request,'home/index.html',{'posts':posts})