from django.conf.urls import url, include
from django.conf.urls.static import static
from webapp.views import DataListView, BarView, AdvancedGraph
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

app_name = 'webapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^csv', views.csv, name='csv'),
    url(r'^rawdata', views.DataListView.as_view(), name='rawdata'),
    url(r'^bar', views.BarView.as_view(), name='bar'),
    url(r'^dbbar', views.AdvancedGraph.as_view(), name='dbbar'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]