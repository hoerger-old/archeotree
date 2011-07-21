from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
    (r'display/(?P<student_id>\d+)/', 'main.views.display'),
    (r'ajax/studentdata', 'main.views.ajax_studentdata'),
)
