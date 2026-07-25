from django.contrib import admin
from .models import Posted,Category,Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':['name']} #slug auto fill hobe


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']

@admin.register(Posted)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','category','status','created_at']
    list_filter=['status','created_at','category']
    search_fields=['title','body']
    list_editable=['status']  #list thake status change kora jabe
    date_hierarchy='created_at'



    
    