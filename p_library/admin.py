from django.contrib import admin
from p_library.models import Book, Author, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'year_release')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    # prevent default publisher from deleting
    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.id == 1:
            return False
        else:
            return True
