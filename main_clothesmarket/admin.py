from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(AboutUs)
admin.site.register(Phone)
admin.site.register(Adress)
admin.site.register(OpeningHours)
admin.site.register(ShopInfo)
admin.site.register(Kind)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available', 'price']
    prepopulated_fields = {'slug':('title',)}
