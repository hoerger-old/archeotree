from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^', 'main.views.index'),
)
