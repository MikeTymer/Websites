from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(BlogComment)
admin.site.register(Contact)
