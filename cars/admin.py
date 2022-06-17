from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):

        def thumbnail(self,object):
            return format_html('<img src="{}" width="40" style="border-radius: 50%;" />'.format(object.car_photo.url))
        thumbnail.short_description='Car-Image'

        list_display = ('id','car_title','thumbnail','city','color','model','year','body_style','is_featured',)
        list_display_links=('id','car_title','thumbnail')
        list_editable= ('is_featured',)
        search_fields=('id','car_title','city','body_style')
        list_filter=('id','city','car_title',)

admin.site.register(car,CarAdmin)