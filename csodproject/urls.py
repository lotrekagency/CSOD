"""csodproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

#https://django-registration.readthedocs.io/en/3.0/
#https://django-registration.readthedocs.io/en/3.0/custom-user.html
#https://django-registration.readthedocs.io/en/3.0/one-step-workflow.html

urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/register/",    #URL per registrazione tramite Broser
         RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url="/",
            ), name="django_registration_register"),

    path("accounts/",
         include("django_registration.backends.one_step.urls")),

    path("accounts/",  #login tramite urls a dispozione grazie a django
         include("django.contrib.auth.urls")),

    path("api/",
         include("users.api.urls")),

    path("api/",
         include("messagestext.api.urls")),

    path("api-auth/",  #login tramite browsableAPI
         include("rest_framework.urls")),

    path("api/rest-auth/",  #login tramite REST.Auth
         include("rest_auth.urls")),

    path("api/rest-auth/registration/",  #registrazione tramite REST.Auth
         include("rest_auth.registration.urls")),

    re_path(r"^.*$",
            IndexTemplateView.as_view(),
            name="entry-point")
    #questo re_path serve a ridizionare qualsiasi richiesta a IndexTemplateView
    #r (roasting e si usa per evitare esclusioni di carattere)
]
