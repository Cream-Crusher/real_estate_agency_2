from django.contrib import admin

from .models import Flat, UserComplaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.apartment.through
    raw_id_fields = ['owner', ]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'address', 'town', ]
    readonly_fields = ['created_at', ]
    list_display = ['address', 'price', 'construction_year', 'town', 'new_building', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', 'has_balcony', 'rooms_number', ]
    inlines = [OwnerInline, ]
    raw_id_fields = ['liked_by', ]


@admin.register(UserComplaint)
class UserComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['apartment', ]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['apartment', ]
