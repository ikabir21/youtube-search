from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ApiKeys)

class VideoModelConfig(admin.ModelAdmin):
    model = Videos
    search_fields = ('title', 'description')
    ordering = ('id', 'publishing_time', 'created_at', 'updated_at')
    list_display = ('id', 'title', 'description', 'publishing_time', 'thumbnails', 'video_uid')


admin.site.register(Videos, VideoModelConfig)