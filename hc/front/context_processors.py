from django.conf import settings


def branding(request):
    return {
        "site_name": settings.SITE_NAME,
        "site_logo_url": settings.SITE_LOGO_URL,
        "site_root": settings.SITE_ROOT
    }
