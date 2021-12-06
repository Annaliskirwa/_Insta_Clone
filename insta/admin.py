from django.contrib import admin
from .models import Image,Comments,Profile

#register
admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Profile)