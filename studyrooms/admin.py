from django.contrib import admin
from .models import *

admin.site.register(Studyroom)


class StudyroomAdmin(admin.ModelAdmin):
    pass

# test
# Register your models here.
