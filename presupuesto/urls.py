# Librerias Django
# Django Libraries
from django.conf import settings
from django.conf.urls import handler404, handler500, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import index, sitemap
from django.urls import path
from django.utils.translation import ugettext_lazy as _
from django.views.static import serve

# Thirdparty Libraries
from usercustom.views import ActivateLanguageView
from graphene_django.views import GraphQLView
from zinnia.sitemaps import (
    AuthorSitemap, CategorySitemap, EntrySitemap, TagSitemap)

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns = [
    path('', include('main.urls')),
    path('', include('usercustom.urls')),
    path('admin/', admin.site.urls),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, }),
    path('blog/', include('zinnia.urls')),
    path('comments/', include('django_comments.urls')),
]

urlpatterns += [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('rosetta/', include('rosetta.urls'))
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path(
        '<language_code>/language/activate/',
        ActivateLanguageView.as_view(),
        name='activate_language'
    ),
)


handler404 = 'usercustom.views.error_404'
handler500 = 'usercustom.views.error_500'
