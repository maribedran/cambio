from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'week.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.dolar, name='dolar'),
    url(r'^dolar/$', views.dolar, name='dolar'),
    url(r'^euro/$', views.euro, name='euro'),
    url(r'^peso/$', views.peso, name='peso'),
    url(r'^admin/', include(admin.site.urls)),
)
