"""deg_authoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from deg_authoring.landing import views 

app_name = 'deg_authoring'
urlpatterns = [
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^deg_authoring/upload$', views.upload_image_view, name='upload_image_view'),
    url(r'^deg_authoring/$', views.game_list, name='game_authoring_list'),
    url(r'^deg_authoring/games/(?P<game_id>[0-9]+)/$', views.game_detail, name='game_detail'),
    url(r'^deg_authoring/editions/$', views.edition_list, name='edition_list'),
    url(r'^deg_authoring/editions/(?P<game_edition_id>[0-9]+)/$', views.edition_detail, name='edition_detail'),
    url(r'^deg_authoring/editions/(?P<game_edition_id>[0-9]+)/save/$', views.save_edition, name='save_edition'),        
    url(r'^institutions/$', TemplateView.as_view(template_name="deg_authoring/institutions.html"), name='institutions'),
    url(r'^sponsored_game/$', TemplateView.as_view(template_name="deg_authoring/sponsored_game.html"), name='sponsored_game'),
    #url(r'^deg_authoring/authoring2_files/$', views.game_list, name='game_authoring_list'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
