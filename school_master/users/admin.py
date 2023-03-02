from django.contrib import admin

# Register your models here.
from .models import User,Gallery
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =['username','name','user_type','is_active',]
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display =['user','image','datetime']
