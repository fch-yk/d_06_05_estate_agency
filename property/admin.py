from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('id', 'created_at',)
    list_display = (
        'id',
        'address',
        'price',
        'new_building',
        'construction_year',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)
    ordering = ('id',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ('id', 'user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('id', 'name', 'pure_phone',)
    readonly_fields = ('id',)
    ordering = ('id',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
