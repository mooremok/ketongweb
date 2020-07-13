from django.contrib import admin
from . models import IndexSer, IndexSpe


@admin.register(IndexSer)
class IndexSerAdmin(admin.ModelAdmin):
	list_display = ['title', 'image', 'description']


@admin.register(IndexSpe)
class IndexSpeAdmin(admin.ModelAdmin):
	list_display = ['title', 'image', 'description']