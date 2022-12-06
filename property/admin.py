from django.contrib import admin

from .models import Flat, Review

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'address', 'town', ]
    readonly_fields = ['created_at', ]
    list_display = ['address', 'price', 'construction_year', 'town', 'new_building', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', 'has_balcony', 'rooms_number', ]
    raw_id_fields = ['liked_by', ]


class ReviewAdmin(admin.ModelAdmin):
    raw_id_fields = ['address', ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Review, ReviewAdmin)