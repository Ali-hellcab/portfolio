from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # ── List View ─────────────────────────────────────────────────────────────
    list_display   = ("title", "category", "is_featured", "date_created", "thumbnail_preview")
    list_filter    = ("category", "is_featured", "date_created")
    search_fields  = ("title", "description", "technologies")
    list_editable  = ("is_featured",)
    ordering       = ("-is_featured", "-date_created")

    # ── Form Layout ───────────────────────────────────────────────────────────
    fieldsets = (
        ("Core Information", {
            "fields": ("title", "slug", "description", "body"),
        }),
        ("Classification", {
            "fields": ("category", "technologies", "is_featured"),
        }),
        ("Media & Links", {
            "fields": ("image", "github_link", "live_link"),
        }),
    )
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields     = ("date_created", "date_updated")

    # ── Custom Column: Thumbnail ───────────────────────────────────────────────
    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;width:80px;object-fit:cover;border-radius:4px;" />',
                obj.image.url,
            )
        return "—"

    thumbnail_preview.short_description = "Preview"

    # ── Custom admin site branding ─────────────────────────────────────────────
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related()


# Admin site global branding
admin.site.site_header  = "Portfolio Admin"
admin.site.site_title   = "Portfolio"
admin.site.index_title  = "Manage Your Portfolio"
