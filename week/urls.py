from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'week.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('week.home.urls', namespace='home')),
    url(r'^admin/', include(admin.site.urls)),
)
