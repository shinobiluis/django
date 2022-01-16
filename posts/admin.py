from django.contrib import admin

# Register your models here.
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'profile', 'title', 'photo')

    # Hacer que al dar click al numero nos abra el registro
    list_display_links = ('pk' ,'user', 'title')