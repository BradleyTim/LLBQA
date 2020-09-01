from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('sw.js', (TemplateView.as_view(template_name="sw.js",content_type='application/javascript',)), name='sw.js'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
