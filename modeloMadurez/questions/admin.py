from django.contrib import admin
from .models import Questionary
# Register your models here.
class QuestionaryAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    list_display = ('name',)

admin.site.register(Questionary,QuestionaryAdmin)