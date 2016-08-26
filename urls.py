from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.utils.functional import curry
from django.views.defaults import page_not_found, permission_denied,\
    server_error

from sfsystem.system.views import errors

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

handler403 = curry(permission_denied, template_name='error/403.html')
handler404 = curry(page_not_found, template_name='error/404.html')
handler500 = curry(errors.server_error, template_name='error/500.html')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'herkules.views.home', name='home'),
    # url(r'^herkules/', include('herkules.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^ajax_select/', include('ajax_select.urls')),
    
    url(r'^user/', include('sfsystem.system.apps.user.urls')),
    url(r'^payment/', include('sfsystem.system.apps.payment.urls')),
    url(r'^money-account/', include('sfsystem.system.apps.money_account.urls')),
    url(r'^carnet/', include('sfsystem.system.apps.carnet.urls')),
    url(r'^finance/', include('sfsystem.system.apps.finance.urls')),
    url(r'^messages/', include('sfsystem.apps.messages_center.urls')),
    url(r'^user/', include('sfsystem.system.apps.facility.urls')),
    url(r'^partners/', include('sfsystem.system.apps.notifications.urls')),
    url(r'^partners/', include('sfsystem.system.apps.partners.urls')),

    url(r'^shop/', include('sfsystem.apps.shop.urls')),
    url(r'^groups/', include('sfsystem.apps.group_classes.urls')),
    url(r'^classrooms/', include('sfsystem.apps.classrooms.urls')),
    url(r'^announcement/', include('sfsystem.apps.announcement.urls')),
    url(r'^card/', include('sfsystem.apps.id_scan_card.urls')),
    url(r'^payment-transferuj/', include('sfsystem.apps.pay_transferuj.urls')),

    url(r'^$', 'sfsystem.system.apps.user.views.dashboard', name='homepage'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SERVE_STATIC:
    urlpatterns = patterns('',
       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
           {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    ) + urlpatterns