from django.conf.urls import url
from . import views
app_name = 'gjk'
urlpatterns = [

    url(r'^$', views.homepage, name='index'),

    url(r'^tag/$', views.tag_articles, name='tag_articles'),

    url(r'^show/$', views.show, name='show'),

    url(r'^manager/$', views.manager, name='manager'),
    url(r'^td/$', views.test_JSdate, name='test_JSdate'),

    # the failed_chart
    url(r'^charts/$', views.charts, name='charts'),

    # url(r'^test_form/$', views.test_form, name='test_form'),
    url(r'^test/$', views.test, name='test'),
    
    url(r'^json/$', views.json, name='json'),
    url(r'^zxt/$', views.zxt, name='zxt'),
    url(r'^data_json/$', views.data_json, name='json1'),
    url(r'^data_dict/$', views.data_dict, name='dict1'),
    url(r'^json/(?P<date1>((\d{4})-(0\d{1}|1[0-2])-(0\d{1}|[12]\d{1}|3[01])))/(?P<date2>((\d{4})-(0\d{1}|1[0-2])-(0\d{1}|[12]\d{1}|3[01])))/$',
             views.json2, name='json2'),


    url(r'^send_email/$', views.send_email, name='send_email'),

]