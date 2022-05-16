from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

class Company(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    mobile = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    status=models.CharField(max_length=10,choices=STATUS)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.title


class Service(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=60, blank=True)
    icon = models.CharField(max_length=20)
    detail = models.CharField(max_length=255)
    short_detail = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)
    portfolio_title = models.CharField(max_length=50)
    portfolio_image = models.ImageField(upload_to='images/')
    portfolio_alt = models.CharField(max_length=60, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class About(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = models.CharField(max_length=300)
    short_detail = models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=60, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title

class Clients(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=60, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name

class Team(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=60, blank=True)
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
    ## Method in creating a fake table in read-only mode
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url)) #defined like this - from django.utils.safestring import mark_safe

    image_tag.short_description = 'Image'


class Strategy(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    mission = models.CharField(max_length=250)
    vision = models.CharField(max_length=250)
    quality = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Strategy'

    def __str__(self):
        return self.mission