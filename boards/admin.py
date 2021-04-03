from django.contrib import admin
from .models import *


admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    pass
