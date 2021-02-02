from django.contrib import admin

# Register your models here.
from .models import BlogPost

# Register your models here.

# Need to register my BlogPost so it shows up in the admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    field = '__all__'
