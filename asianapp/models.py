from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.timezone import datetime

class Header(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to='uploads/')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.phone

class Slider(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    details = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads')
    sort_order = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    details = models.TextField()
    meta_title = models.CharField(max_length=100, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.CharField(max_length=500,null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone1 = models.CharField(max_length=256,null=True, blank=True)
    phone2 = models.CharField(max_length=256,null=True, blank=True)
    website_url = models.URLField(max_length=256,null=True, blank=True)
    fax = models.CharField(max_length=256,null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.address

class Category(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    video_url = models.CharField(max_length=500,null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.video_url

    def __str__(self):
        return self.title

class SocialLink(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    css_class_name = models.CharField(max_length=50,null=True, blank=True)
    social_url = models.URLField(max_length=256,null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class NewsUpdate(models.Model):
    title = models.CharField(max_length=256)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Advertisement(models.Model):
    title = models.CharField(null=True, blank=True, max_length=256)
    details = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/')
    status = models.BooleanField(default=True)
    sort_order = models.IntegerField()
    social_url = models.URLField(max_length=256,null=True, blank=True)
    is_featured = models.BooleanField(default=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class CustomerEmail(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    customeremails = models.EmailField()
    customermessage = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.firstname
