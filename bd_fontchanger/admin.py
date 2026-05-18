from django.contrib import admin

from .models import Font, FontConfig
# Register your models here.


# Create your views here.
class FontSlotInline(admin.TabularInline):
    fields = ("role", "file", "size")

    model = Font
    extra = 0


@admin.register(FontConfig)
class FontConfigAdmin(admin.ModelAdmin):
    inlines = (FontSlotInline,)
    list_display = ("name",)
    exclude = ("name",)

    def has_add_permission(self, request):
        return not FontConfig.objects.exists()
