import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


# 栏目
@python_2_unicode_compatible
class LanMu(models.Model):
    lanmu = models.CharField('栏目', max_length=256)

    def __str__(self):
        return self.lanmu

    class Meta:
        verbose_name = '栏目'


# 标签
@python_2_unicode_compatible
class Column(models.Model):
    lanmu = models.ForeignKey(LanMu, blank=True, null=True, verbose_name='所属栏目')
    name = models.CharField('column_name', max_length=256)
    intro = models.TextField('introduction', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'column'
        verbose_name_plural = '标签'
        ordering = ['name']


@python_2_unicode_compatible
class Article(models.Model):
    set_top = models.BooleanField('设为置顶', default=False)
    author = models.ForeignKey(User, null=True, related_name="author")
    pic = models.ImageField('文章标头图片245x200', upload_to='uploads/blog/images/',
                            default='uploads/blog/images/default.jpg')
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name='小标签')
    title = models.CharField(verbose_name="标题", max_length=256)
    summary = models.TextField(verbose_name="概要", default=" ")
    content = UEditorField('内容', height=500, width=1200,
        default='', blank=True, imagePath="uploads/images/%(basename)s_%(datetime)s.%(extname)s",
        toolbars='full', filePath='uploads/files/%(basename)s_%(datetime)s.%(extname)s')
    pub_date = models.DateTimeField(verbose_name="发表时间")
    see_num = models.IntegerField(verbose_name="浏览数")
    comment_num = models.IntegerField(default=0)
    published = models.BooleanField("发布|热点F", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = '文章'
        ordering = ['-id']


@python_2_unicode_compatible
class Comment(models.Model):
    user = models.ForeignKey(User, null=True)
    article = models.ForeignKey(Article, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'

"""
@python_2_unicode_compatible
class FrendLink(models.Model):
    name = models.CharField("名称描述", max_length = 122)
    url = models.CharField("链接", max_length = 122)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友链'


class Resource(models.Model):
    img = models.ImageField('资源图片670x280', upload_to='uploads/blog/images/',
                            default='uploads/blog/images/resource_default.jpg')
    title = models.CharField("资源标题", max_length=222, default='')
    url = models.CharField("链接URL", max_length=111, default="#")
    desc = models.TextField("资源描述", max_length=222, default='')
    upload_user = models.ForeignKey(User, null=True, related_name="up_user")
    view_url =  models.CharField("预览URL", max_length=111, default="#")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '资源'
		
"""



