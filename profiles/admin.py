from django.contrib import admin
from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'tg_id')
    readonly_fields = ('tg_id', )
    
