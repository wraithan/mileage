from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.graph'),

    (r'^(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/wraithan/devel/mileage/mileage/media'}),

    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
