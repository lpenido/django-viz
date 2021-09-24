from django.contrib import admin

from .models import Record, ScavengerPin

# Register your models here.
admin.site.register(Record)
admin.site.register(ScavengerPin)