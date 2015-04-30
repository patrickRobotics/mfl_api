from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from common.views import APIRoot, root_redirect_view


apipatterns = patterns(
    '',
    url(r'^$', login_required(APIRoot.as_view()), name='root_listing'),
    url(r'^explore/', include('rest_framework_swagger.urls')),
    url(r'^common/', include('common.urls', namespace='common')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^facilities/', include('facilities.urls', namespace='facilities')),
    url(r'^chul/', include('chul.urls', namespace='chul')),
    url(r'^gis/', include('mfl_gis.urls', namespace='mfl_gis')),
)

urlpatterns = patterns(
    '',
    url(r'^$', root_redirect_view, name='root_redirect'),
    url(r'^api/', include(apipatterns, namespace='api')),
    url(r'^accounts/',
        include('users.urls', namespace='mfl_users')),
    url(r'^api/token/', 'rest_framework.authtoken.views.obtain_auth_token'),
)
