from django.conf.urls import url, include
from django.conf.urls.static import static
from webapp.views import AdvancedGraph, PowerGraph
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

app_name = 'webapp'

urlpatterns = [
    url(r'^$', views.loading, name='loading'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^index', views.index, name='index'),
    url(r'^csv', views.csv, name='csv'),
    url(r'^weather', views.weather, name='weather'),
    url(r'^dbbar', views.AdvancedGraph.as_view(), name='dbbar'),
    url(r'^powbar', views.PowerGraph.as_view(), name='powbar'),
]
	
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]