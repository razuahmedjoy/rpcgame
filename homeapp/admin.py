from django.contrib import admin
from .models import *
# Register your models here.
class Adminplayer(admin.ModelAdmin):
    list_display = ['id','name','points']

admin.site.register(player,Adminplayer)