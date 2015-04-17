from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','article.views.home'),
    url(r'^(?P<my_args>\d+)/$','article.views.details', name='details'),
    url(r'^$','article.views.home'),
)
