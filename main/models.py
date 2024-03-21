from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    post_date = models.DateField(default=date.today)
    slug = models.CharField(max_length=100, null=True, blank=True)
    featured_image = models.ImageField(upload_to='images/category/')

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    description = models.TextField()
    mini_description = models.TextField()
    post_date = models.DateField(default=date.today)
    slug = models.CharField(max_length=100, null=True, blank=True)
    feature_image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " ==> " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.post_date))
        return super().save(*args, **kwargs)

   
class BlogComment(models.Model):
    description = models.TextField(help_text="Write your comment")
    #name = models.CharField(max_length=30, help_text ="Write your full name here")
    #author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=250)
    contact_date = models.DateTimeField(default=date.today)
    phone_number = models.IntegerField()
    contact_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return str(self.first_name + " " + self.last_name)