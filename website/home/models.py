from django.db import models

# Create your models here.
class Post(models.Model):
	post_title = models.CharField(max_length=300)
	post_description = models.TextField()
	post_status = models.CharField(max_length=30)
	pub_date = models.DateTimeField('date published')
	post_image = models.ImageField(upload_to='uploads/',null='TRUE')

