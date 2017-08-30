from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [

    url(r'^$', views.homepage, name='home'),
    url(r'^resourses/$', views.resourses, name='resource'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^timelines/$', views.timelines, name='timelines'),

    ## 二级页面
    # 栏目组合页面
    url(r'^lanmu/(?P<lm_id>[0-9]+)/$', views.lanmu, name='blog_lanmu'),
    # 分类的标签页面 - tag=column
    # 
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name='tag'),
    
    # 详情页页面
    url(r'^detail/(?P<article_id>[0-9]+)/$', views.detail, name='blog_detail'),
    
    # 关于我们
    url(r'^aboutme/$', views.about_me, name='aboutme'),


    # 发送邮件
    url(r'^send_email/$', views.send_email, name='send_email'),

    ## 分页
    url(r'^split/$', views.split, name='split'),

]