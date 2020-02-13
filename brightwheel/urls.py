"""brightwheel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import urls
from rest_framework import permissions
from drf_yasg import views
from drf_yasg import openapi
from django.conf.urls.static import static
from . import settings
from rest_framework.documentation import include_docs_urls


schema_view = views.get_schema_view(
   openapi.Info(
      title="Brightwheel API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    urls.url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
             name='schema-redoc'),
    urls.url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None),
             name='schema-swagger-ui'),
    urls.url(r'^docs/', include_docs_urls(title='Brightwheel API', public=True)),

    urls.url(r'^email/', urls.include('brightwheelemail.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
