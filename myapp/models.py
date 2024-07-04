from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    # content = models.TextField()
    content = HTMLField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    writer_name = models.CharField(max_length=100)

    def clean(self):
        if not self.image and not self.image_url:
            raise ValidationError(
                'Either an image file or an image URL must be provided.')

    def formatted_content(self):
        # Use mark_safe to render content as HTML
        return mark_safe(self.content)

    formatted_content.allow_tags = True  # Allow HTML tags to render in admin

    def __str__(self):
        return self.title
