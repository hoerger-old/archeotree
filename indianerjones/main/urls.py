from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
    (r'^index.html$', 'main.views.index'),
)
