from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Snack
# Register your models here.

admin.site.register(Snack)
class AdminThing(admin.ModelAdmin):
    list_display= ['name', 'reviewer']
    search_fields = ['name']
    list_display_links = ('reviewer',)
