from django.contrib import admin

from .models import Gallery, Images, Project

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'service', 'status']
    list_filter = ['service']
    readonly_fields = ['image_tag']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'service', 'status', 'image_tag']
    list_filter = ['service']