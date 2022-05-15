from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from home.models import Service

class Project(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    service = models.ForeignKey(Service, related_name='project', on_delete=models.CASCADE) #many to one relation with Service
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=60, blank=True)
    client = models.CharField(max_length=50)
    launched = models.CharField(max_length=50)
    demands = models.CharField(max_length=50)
    detail = models.CharField(max_length=255)
    short_detail = models.CharField(max_length=255)
    video_link = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse('project:project_detail', args=[self.slug])
    
    def __str__(self):
        return self.title


## Method in creating a fake table in read-only mode
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url)) #defined like this - from django.utils.safestring import mark_safe

    image_tag.short_description = 'Image'

    
class Images(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE) #many to one relation with Product
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    service = models.ForeignKey(Service, related_name='gallery', on_delete=models.CASCADE) #many to one relation with Service
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=60, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.title


## Method in creating a fake table in read-only mode
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url)) #defined like this - from django.utils.safestring import mark_safe

    image_tag.short_description = 'Image'