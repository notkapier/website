from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
# Create your models here.
class PostStatus(models.Model):
	def __str__(self):
		return self.post_status
	post_status = models.CharField(max_length=300)
	class Meta:
		verbose_name_plural="Post Statuses"
class Post(models.Model):
	def __str__(self):
		return self.post_title
	post_title = models.CharField(max_length=300)
	post_description = models.TextField()
	status = models.ForeignKey(PostStatus,on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	post_image = models.ImageField(upload_to='uploads/',null='TRUE')

class Announcement(models.Model):
	announcement_title = models.CharField(max_length=300)
	pub_date = models.DateTimeField('date published',null='TRUE')
	announcement_attachment = models.FileField(upload_to='uploads',null='TRUE')

class Course(models.Model):
	def __str__(self):
		return self.course_name
	course_name = models.CharField(max_length=300)
	course_description = models.TextField()

class Batch(models.Model):
	def __str__(self):
		return "%s - %s" %(self.batch_year,self.course)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	batch_year = models.IntegerField(('year graduated'),choices=YEAR_CHOICES,default=datetime.datetime.now().year)
	class Meta:
		verbose_name_plural="batches"

class Library(models.Model):
	library_name = models.CharField(max_length=300)
	def __str__(self):
		return self.library_name
	class Meta:
		verbose_name_plural="Libraries"
class Reference(models.Model):
	reference_title = models.CharField(max_length=300)
	library = models.ForeignKey(Library,on_delete=models.CASCADE)
	reference_description = models.TextField()
	reference_attachment = models.FileField(upload_to='uploads',null='TRUE')
class Traccer(models.Model):
	def __str__(self):
		return self.traccer_type
	traccer_type = models.CharField(max_length=300)
	traccer_image = models.ImageField(upload_to='uploads/',null='TRUE')
class Element(models.Model):
	def __str__(self):
		return self.element_name
	element_name = models.CharField(max_length=300)
	element_description = models.TextField()
	element_image = models.ImageField(upload_to='uploads/',null='TRUE')
	element_attachment = models.FileField(upload_to='uploads/',null='TRUE')
class TraccerItem(models.Model):
	traccer = models.ForeignKey(Traccer,on_delete=models.CASCADE)
	traccer_item_title = models.CharField(max_length=300)
	traccer_item_description = models.TextField()
	traccer_item_image = models.ImageField(upload_to='uploads/',null='TRUE')
	traccer_item_attachment = models.FileField(upload_to='uploads/',null='TRUE')


