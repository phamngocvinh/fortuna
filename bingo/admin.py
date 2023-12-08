from django.contrib import admin

from .models import BingoCard


class SettingAdmin(admin.ModelAdmin):
    list_display = ('userid', 'date', 'numbers')


admin.site.register(BingoCard, SettingAdmin)
