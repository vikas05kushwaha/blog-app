from django.contrib import admin
from home.models import Blog, Contact ,Tag
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Tag)
