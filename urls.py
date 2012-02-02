from django.conf.urls.defaults import *
from bookmarks.views import *

urlpatterns = patterns('',
    (r'^$', main_page),
)
