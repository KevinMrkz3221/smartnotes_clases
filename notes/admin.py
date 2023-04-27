from django.contrib import admin

from . import models
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created')


admin.site.register(models.Notes, NotesAdmin)