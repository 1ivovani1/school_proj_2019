from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Note)

# Register your models here.
