'''
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from links_api import urls as links_urls
from rest_framework.permissions import AllowAny

SCHEMA_VIEW = get_schema_view(
    openapi.Info(
        title="Link Aggregator API",
        default_version='v1',
        description="API documentation for Link Aggregator",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/links', include(links_urls)),
    path('docs', SCHEMA_VIEW.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
