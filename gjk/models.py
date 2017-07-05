from django.db import models

from django.db import models
from DjangoUeditor.models import UEditorField


from news.models import Categary


class Article(models.Model):
    # toutiao = models.BooleanField('设为头条',default=False)
    # pic = models.ImageField('头条图片436*200',upload_to='uploads/top_images/',default='uploads/top_images/default.jpg')
    title = models.CharField('标题',max_length=255)
    column = models.ForeignKey(Categary, verbose_name = "类别")
    img = UEditorField('手机端缩略图', height=200, width=500,
                           default='', blank=True, imagePath="uploads/images/%(basename)s_%(datetime)s.%(extname)s",
                           toolbars='full', filePath='uploads/files/%(basename)s_%(datetime)s.%(extname)s')
    abstract = models.TextField('摘要', default='', blank=True)
    content = UEditorField('内容', height=500, width=1200,
        default='', blank=True, imagePath="uploads/images/%(basename)s_%(datetime)s.%(extname)s",
        toolbars='full', filePath='uploads/files/%(basename)s_%(datetime)s.%(extname)s')
    # published = models.BooleanField('正式发布',default=True)
    # pub_date = models.DateTimeField('发表日期')
    author = models.CharField('作者',default='清朗安全',max_length=255)
    sourcefrom = models.CharField('来源描述',default='清朗安全',max_length=255)
    slug_url = models.CharField('默认网址勿改',default='/',max_length=255)
    # slug_name = models.CharField('默认栏目名勿改',default='安全热点',max_length=255)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "稿件库文章"
    
    

