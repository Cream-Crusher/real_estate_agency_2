from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'address', 'town', ]
    readonly_fields = ['created_at', ]
    list_display = ['address', 'price', 'construction_year', 'town', 'new_building', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', 'has_balcony', 'rooms_number', ]

admin.site.register(Flat, FlatAdmin)
