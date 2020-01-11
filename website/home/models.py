from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
YEAR_CHOICES = []
for r in range(1978, (datetime.datetime.now().year+1)):
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
	post_description = RichTextUploadingField()
	status = models.ForeignKey(PostStatus,on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	post_image = models.ImageField(upload_to='uploads/',null='TRUE')

class Announcement(models.Model):
	def __str__(self):
		return self.announcement_title
	announcement_title = models.CharField(max_length=300)
	pub_date = models.DateTimeField('date published',null='TRUE')
	announcement_attachment = models.FileField(upload_to='uploads',null='TRUE')
	@property
	def filename(self):
		return self.announcement_attachment.path

class Course(models.Model):
	def __str__(self):
		return self.course_name
	course_abv = models.CharField(max_length=10)
	course_name = models.CharField(max_length=300)
	course_description = models.TextField()
	@classmethod
	def getAllCourses(self):
		try:
			courses = Course.objects.all()
		except Course.DoesNotExist:
			courses = None
		return courses

class Batch(models.Model):
	def __str__(self):
		return "%s - %s" %(self.batch_year,self.course)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	batch_year = models.IntegerField(('year graduated'),choices=YEAR_CHOICES,default=datetime.datetime.now().year)
	batch_image = models.ImageField(upload_to='uploads/',null='TRUE')
	class Meta:
		verbose_name_plural="batches"
		unique_together = ('course_id','batch_year')
	@classmethod
	def getAllBatches(self):
		try:
			batches = Batch.objects.order_by('-batch_year').all()
		except Batch.DoesNotExist:
			batches = None
		return batches
class BatchImage(models.Model):
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
	batch_image_description = models.CharField(max_length=300)
class Library(models.Model):
	library_name = models.CharField(max_length=300)
	def __str__(self):
		return self.library_name
	class Meta:
		verbose_name_plural="Libraries"
	@classmethod
	def getAllLibraries(self):
		try:
			libraries = Library.objects.all()
		except Library.DoesNotExist:
			libraries = None
		return libraries 
class Reference(models.Model):
	def __str__(self):
		return self.reference_title
	reference_title = models.CharField(max_length=300)
	library = models.ForeignKey(Library,on_delete=models.CASCADE)
	reference_description = models.TextField()
	pub_date = models.DateTimeField('date published',null='TRUE')
	reference_attachment = models.FileField(upload_to='uploads',null='TRUE')
	@classmethod
	def getAllReference(self,library_id):
		try:
			references = Reference.objects.filter(library_id=library_id)
		except Reference.DoesNotExist:
			references = None
		return references
	@property
	def filename(self):
		return self.reference_attachment.path
	
class Traccer(models.Model):
	def __str__(self):
		return self.traccer_type
	traccer_type = models.CharField(max_length=300)
	traccer_image = models.ImageField(upload_to='uploads/',null='TRUE')
	def __str__(self):
		return self.traccer_type
	class Meta:
		verbose_name_plural="Traccers"
	@classmethod
	def getAllTraccers(self):
		try:
			traccers = Traccer.objects.all()
		except Traccer.DoesNotExist:
			traccers = None
		return traccers 
class Element(models.Model):
	def __str__(self):
		return self.element_name
	element_name = models.CharField(max_length=300)
	element_description = models.TextField()
	element_image = models.ImageField(upload_to='uploads/',null='TRUE',blank='TRUE')
	element_attachment = models.FileField(upload_to='uploads/',null='TRUE',blank='TRUE')

	@classmethod
	def getbanner(self):
		try:
			banner = Element.objects.get(element_name='banner')
		except Element.DoesNotExist:
			banner = Element(element_name='banner',element_description='Default Banner',element_image='/uploads/home.jpg')
		return banner
	def getlogo(self):
		try:
			logo = Element.objects.get(element_name='logo')
		except Element.DoesNotExist:
			logo = Element(element_name='logo',element_description='Default Logo',element_image='/uploads/logo_lAoTIdl.jpg')
		return logo

class TraccerItem(models.Model):
	traccer = models.ForeignKey(Traccer,on_delete=models.CASCADE)
	traccer_item_title = models.CharField(max_length=300)
	traccer_item_description = models.TextField()
	traccer_item_image = models.ImageField(upload_to='uploads/',null='TRUE')
	traccer_item_attachment = models.FileField(upload_to='uploads/',null='TRUE')
	def __str__(self):
		return self.traccer_item_title
	@property
	def filename(self):
		return self.traccer_item_attachment.path
	@classmethod
	def getAllTraccerItem(self,traccer_id):
		try:
			tracceritems = TraccerItem.objects.filter(traccer_id=traccer_id)
		except Reference.DoesNotExist:
			tracceritems = None
		return tracceritems


