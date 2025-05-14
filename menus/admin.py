from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ("parent", "title", "url", "sort_order")
    ordering = ("sort_order",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "verbose_name")
    inlines = (MenuItemInline,)
