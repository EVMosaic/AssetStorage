"""AssetStorageDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from AssetStorage import views


urlpatterns = [
    url(r'^$', views.SearchView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^detail/(?P<pk>[-\w]+)/$', views.AssetDetailView.as_view(), name='asset-detail'),
    url(r'^upload/', views.UploadView.as_view()),
    url(r'^simple/(?P<pk>[0-9]+)/', views.SimpleAssetView.as_view(), name='simple-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]