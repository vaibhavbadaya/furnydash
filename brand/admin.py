from .models import Brand # Import your models
from django.contrib import admin




@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



admin.site.site_header = 'FurnyDash'
admin.site.site_title = 'FurnyDash'
admin.site.index_title = 'Brand Management'


