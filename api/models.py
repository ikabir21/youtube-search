from django.db import models

# Create your models here.

class ApiKeys(models.Model):
    key = models.CharField(null=False, blank=False, max_length=100)
    
    class Meta:
        verbose_name = "Key"
    def __str__(self):
        return self.key

class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    publishing_time = models.DateTimeField()
    thumbnails = models.URLField(max_length=200)
    video_uid = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Video"
    
    def __str__(self):
        return self.title