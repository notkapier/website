from django.contrib import admin

# Register your models here.
from .models import Post,Announcement,Course,Batch,Library,Reference,Traccer,TraccerItem,Element,PostStatus,AboutTab,Alumnus

admin.site.register(Post)
admin.site.register(Announcement)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Library)
admin.site.register(Reference)
admin.site.register(Traccer)
admin.site.register(TraccerItem)
admin.site.register(Element)
admin.site.register(PostStatus)
admin.site.register(AboutTab)
admin.site.register(Alumnus)