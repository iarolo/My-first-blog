from django.contrib import admin

from blog.models import Post
from .models  import Post

admin.site.register(Post)

