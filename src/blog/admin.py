from django.contrib import admin

# Register your models here.

from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated",)
    list_editable = ("published", )


#dire qu'on souhaite afficher cette class dans notre interface d'admin
admin.site.register(BlogPost, BlogPostAdmin)