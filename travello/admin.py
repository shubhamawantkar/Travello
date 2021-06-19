from travello.models import Destination
from django.contrib import admin
from .models import Destination
# Register your models here.


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

    
admin.site.register(Destination, DestinationAdmin)