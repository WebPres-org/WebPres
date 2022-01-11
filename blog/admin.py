from django.contrib import admin
from .models import Post, Categories, PostComment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    #list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)
admin.site.register(Categories)
