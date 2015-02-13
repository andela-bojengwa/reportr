from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'', include('apps.home.urls')),

    # Register Home Views
    # url(r'^$', include(core.urls)),

    # Register Admin Views
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'home/login.html'}, name='login'),
    url(r'^auth/', include('social_auth.urls')),
)
