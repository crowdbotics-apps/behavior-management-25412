from django.contrib import admin
from .models import Behavior, Originator, Week


class BehaviorAdmin(admin.ModelAdmin):
    list_display = [
        "__str__", "trigger", "behavior", "intensity", "consequence", "date"
    ]
    search_fields = ["originator__name"]


admin.site.register(Behavior, BehaviorAdmin)
admin.site.register(Week)
admin.site.register(Originator)

# Register your models here.
