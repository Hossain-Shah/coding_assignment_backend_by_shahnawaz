from django.contrib import admin

from Inventory.models import Inventory
from Inventory.models import Supplier


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "stock",
        "supplier",
    )
    search_fields = ("name", "supplier", "stock", "description")
    list_filter = ("name", "supplier", "availability")
    ordering = ("name",)


class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name"
    )
    list_filter = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("id", "name")


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
