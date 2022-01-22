from django.contrib import admin
from .models import Distillery, Whisky


class DistilleryAdmin(admin.ModelAdmin):
    pass


class WhiskyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Distillery, DistilleryAdmin)
admin.site.register(Whisky, WhiskyAdmin)
