from django.contrib import admin
from .models import Post,Profile,Like,Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Comment)