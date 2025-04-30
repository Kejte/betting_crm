from django.contrib import admin
from profiles.models import Profile, ReferalProgramAccount


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'tg_id')
    readonly_fields = ('tg_id', )
    search_fields = ('username',)

@admin.register(ReferalProgramAccount)
class ReferalProgramAccountAdmin(admin.ModelAdmin):
    list_display = ('profile',)
    search_fields = ('profile__pk',)