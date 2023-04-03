from django.contrib import admin

# Register your models here.
from .models import Post ,Author, Tag, Comment #Import Model to register


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email" ]
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["Author", "caption", "date", ]
    list_display = ["title", "date", "Author", ]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name", "post")