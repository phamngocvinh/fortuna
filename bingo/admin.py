from django.contrib import admin

from .models import BingoCard, System


class BingoSetting(admin.ModelAdmin):
    list_display = ('userid', 'date', 'numbers', 'create_datetime')


class SystemSetting(admin.ModelAdmin):
    list_display = ('lock_submit',)


admin.site.register(BingoCard, BingoSetting)
admin.site.register(System, SystemSetting)
