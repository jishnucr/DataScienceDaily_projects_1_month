from django.contrib import admin
from .models import webdata

class PostAdmin(admin.ModelAdmin):
    list_display=['title','created_date']
    list_filter=['title','created_date']
    search_fields=['title']
    
    
# Register your models here.
admin.site.register(webdata,PostAdmin)
