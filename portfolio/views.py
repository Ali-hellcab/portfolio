from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST
from .models import Project
import json

def index(request):
    """
    Main landing page — fetches all projects, separated by category, and passes skills.
    Template: portfolio/index.html
    """
    all_projects     = Project.objects.all()
    backend_projects = all_projects.filter(category=Project.Category.BACKEND)
    ml_projects      = all_projects.filter(category=Project.Category.ML)
    full_projects    = all_projects.filter(category=Project.Category.FULLSTACK)
    featured         = all_projects.filter(is_featured=True)

    context = {
        "projects":          all_projects,
        "backend_projects":  backend_projects,
        "ml_projects":       ml_projects,
        "full_projects":     full_projects,
        "featured_projects": featured,
        # Skills lists added to the main context
        "backend_skills":    ["Python", "Django", "DRF", "PostgreSQL", "SQLite", "Redis", "REST APIs", "Docker", "AWS", "Git"],
        "ml_skills":         ["PyTorch", "TensorFlow", "scikit-learn", "HuggingFace", "CNNs", "LSTMs", "Pandas", "NumPy", "Matplotlib", "FastAPI"],
    }
    return render(request, "portfolio/index.html", context)


def project_detail(request, slug):
    """
    Optional detail page for a single project.
    Template: portfolio/project_detail.html
    """
    project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/project_detail.html", {"project": project})


@require_POST
def contact(request):
    """
    Handles the AJAX contact form submission.
    Returns JSON so the frontend can show a success/error message without a full reload.
    """
    try:
        data    = json.loads(request.body)
        name    = data.get("name", "").strip()
        email   = data.get("email", "").strip()
        message = data.get("message", "").strip()

        if not all([name, email, message]):
            return JsonResponse({"ok": False, "error": "All fields are required."}, status=400)

        # ── Send email (configure EMAIL_* in settings.py first) ──────────────
        subject  = f"Portfolio Contact: {name}"
        body     = f"From: {name} <{email}>\n\n{message}"
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],   # defined in settings.py
            fail_silently=False,
        )
        return JsonResponse({"ok": True, "message": "Message sent! I'll be in touch soon."})

    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=500)