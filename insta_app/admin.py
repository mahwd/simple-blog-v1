from django.contrib import admin
from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'slug']
    list_display_links = ['title', 'publish_date']
    list_filter = ['publish_date']
    search_fields = ['title']
    list_per_page = 10

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
