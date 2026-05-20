from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """
    Represents a portfolio project entry.
    Manage all projects via the Django Admin panel at /admin/
    """

    class Category(models.TextChoices):
        BACKEND   = "Backend",   "Backend Engineering"
        ML        = "ML",        "Machine Learning"
        FULLSTACK = "Fullstack", "Full Stack"

    # ── Core Fields ──────────────────────────────────────────────────────────
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=220, unique=True, blank=True,
                                   help_text="Auto-filled from title. Used in URLs.")
    description = models.TextField(help_text="Short summary shown on the project card (2–3 sentences).")
    body        = models.TextField(
        blank=True,
        help_text="Long-form Markdown/plain-text description for a detail page (optional)."
    )

    # ── Classification ────────────────────────────────────────────────────────
    category    = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.BACKEND,
    )
    technologies = models.CharField(
        max_length=500,
        help_text="Comma-separated list of tech tags, e.g. 'Python, Django, PostgreSQL, REST API'",
    )

    # ── Media & Links ─────────────────────────────────────────────────────────
    image        = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        help_text="Upload a project screenshot or cover image.",
    )
    github_link  = models.URLField(blank=True, help_text="GitHub repository URL.")
    live_link    = models.URLField(blank=True, help_text="Live demo / deployment URL.")

    # ── Meta ──────────────────────────────────────────────────────────────────
    is_featured  = models.BooleanField(default=False,
                                       help_text="Pin featured projects to the top of the grid.")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "-date_created"]
        verbose_name        = "Project"
        verbose_name_plural = "Projects"

    # ── Helpers ───────────────────────────────────────────────────────────────
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        """Returns technologies as a Python list, stripped of whitespace."""
        return [t.strip() for t in self.technologies.split(",") if t.strip()]

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"
