from django.db import models
from PIL import Image

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.category

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    projectId = models.AutoField(primary_key=True, auto_created=True)
    project_title = models.CharField(max_length=200)
    project_timeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    project_descriptions = models.TextField()
    project_youtubeUrl = models.TextField(blank=True)
    project_image = models.ImageField(blank=True, null=True)

    def sace(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.project_image.path)
        if img.height > 300 or img.weight > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.project_image.path)

