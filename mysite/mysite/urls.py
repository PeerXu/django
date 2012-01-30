from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, processors_demo
from books.views import book_info
from demos.views import view_tags, view_tags_current_time, view_tags_current_time2, view_tags_current_time3

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    ('^hello$', hello),
    ('^current_datetime$', current_datetime),
    ('^processors_demo$', processors_demo),
    ('^book/info$', book_info),
    ('^demo/tags/demo0$', view_tags),
    ('^demo/tags/current_time$', view_tags_current_time),
    ('^demo/tags/current_time2$', view_tags_current_time2),
    ('^demo/tags/current_time3$', view_tags_current_time3),
)
