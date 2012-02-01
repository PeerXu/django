from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, processors_demo
from books.views import book_info
from demos.views import *

from django.views.generic.base import TemplateView

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
    ('^demo/test', view_demos_test_template),
    ('^demo/tags/filter$', view_tags_filter),
    ('^demo/tags/current_time$', view_tags_current_time),
    ('^demo/tags/current_time2$', view_tags_current_time2),
    ('^demo/tags/current_time3$', view_tags_current_time3),
    ('^demo/tags/my_comment$', view_tags_my_comment),
    ('^demo/tags/my_upper$', view_tags_my_upper),

    (r'^about/$', TemplateView.as_view(template_name='about.html'))
    
)
