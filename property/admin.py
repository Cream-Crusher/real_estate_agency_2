from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.apartment_owner.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'address', 'town', ]
    readonly_fields = ['created_at', ]
    list_display = ['address', 'price', 'construction_year', 'town', 'new_building', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', 'has_balcony', 'rooms_number', ]
    raw_id_fields = ['liked_by', ]
    inlines = [OwnerInline, ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['address', ]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['apartment_owner']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
