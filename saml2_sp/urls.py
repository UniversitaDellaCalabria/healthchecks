"""djangosaml2_sp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from djangosaml2 import views

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

saml2_url_prefix = ''

urlpatterns = [
    path('{}/acs/'.format(saml2_url_prefix),
                          views.AssertionConsumerServiceView.as_view(), name='saml2_acs'),

    path(f'{saml2_url_prefix}', include('djangosaml2.urls')),

    # system local
    path('logout/', LogoutView.as_view(),
                            {'next_page': settings.LOGOUT_REDIRECT_URL},
                            name='logout'),
]
