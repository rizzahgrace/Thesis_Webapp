from django.conf.urls import url, include
from django.conf.urls.static import static
from webapp.views import DataListView, BarView
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

app_name = 'webapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^csv', views.csv, name='csv'),
    url(r'^rawdatalist', views.rawdatalist, name='rawdatalist'),
    url(r'^rawdata', views.DataListView.as_view(), name='rawdata'),
    url(r'^chart', views.plot, name='chart'),
    url(r'^bar', views.BarView.as_view(), name='bar'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]