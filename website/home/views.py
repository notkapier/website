from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	return render(request,'home/index.html',{'posts':posts})