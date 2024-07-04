from django.contrib import admin
from .models import Post, Category
from django.db import models
# Register your models here.


# Register your models here.


from tinymce.widgets import TinyMCE


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


admin.site.register(Post, PostAdmin)

admin.site.register(Category)
