from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import re
from .models import Article, Column, LanMu, Comment, Resource
# Create your views here.
import random
import numpy as np


def index(request):
    return HttpResponseRedirect("/blog/")


def common_content(blog=None):
    if blog:
        simmilar_blogs = [x for x in Article.objects.all() if x.column == blog.column]
    else:
        simmilar_blogs = None 
    
    all_tags = Column.objects.all()
    item_ids = [random.randint(1, len(Article.objects.all())) for i in range(10)]
    rand_blogs = [Article.objects.get(id=x) for x in np.unique(item_ids)[:5]]

    right = {"all_tags": all_tags,
        "s_blogs": simmilar_blogs, 
        "item_ids": item_ids,
        "rand_blogs": rand_blogs,
        "lms": LanMu.objects.all(),
        "keyword": False,
        "home": False, 
        }
    return right


def detail(request, article_id):

    blog = Article.objects.get(id=int(article_id))
    conmments = Comment.objects.filter(article=blog)
    num = blog.see_num
    Article.objects.filter(id=article_id).update(see_num = num+1)

    return render(request, "blog/detail.html", {
        
        "blog": blog,
        "right":common_content(blog),
        })


def lanmu(request, lm_id):
    blogs = [ x  for x in Article.objects.all() if x.column.lanmu.id == int(lm_id)]

    return render(request, "blog/article.html", {
        "blogs":blogs,
        "right": common_content(),     
    })



from .forms import ContactForm
def send_email(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'blog/send_email.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = ContactForm(request.POST)
        # 探究搜索关键词为空的内容// 搜素全部为 .
        from django.core import mail
        from django.core.mail import send_mail
        from django.conf import settings
        from django.core.mail import EmailMultiAlternatives
        
        from_email = settings.DEFAULT_FROM_EMAIL

        subject = request.POST["title"]
        content = request.POST["content"]

        # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
        msg = EmailMultiAlternatives(
                subject, 
                content, 
                'actanble@163.com', 
                ["m13429888211@163.com", "actanble@163.com"], #"2970090120@qq.com"
        )
        
        msg.content_subtype = "html"
        
        # 添加附件（可选）
        # msg.attach_file('F:\\TEST\\msg\\tests.pdf')
        
        # 发送
        msg.send()

        return HttpResponse("发送成功！")
    return render(request, 'blog/send_email.html', {
            'form': form,
        })


def tag(request, tag_id):
    blogs  = [x for x in Article.objects.all() if x.column.id == int(tag_id) ]

    return render(request, "blog/article.html", {
        "blogs":blogs,
        "right": common_content(),     
        })


def homepage(request):
    blogs = Article.objects.all()
    
    right = common_content()
    right["home"] = True
    return render(request, "blog/home.html", {
        "blogs":blogs,
        "right": right,     
        }
    )


def about_me(request):
    return render(request, "blog/about.html", {})


def resourses(request):
    # resourses = Resource.objects.all()
    return render(request, "blog/resource.html", )

def articles(request):
    blogs  = Article.objects.all()

    return render(request, "blog/article.html", {
        "blogs":blogs,
        "right": common_content(),     
        })


def timelines(request):
    contents = Article.objects.all().order_by("-pub_date")
    year = []
    year_nums = np.unique([x.pub_date.date().year for x in contents])
    for i in range(len(year_nums)):
        temp_year = {}
        temp_year.setdefault("num", year_nums[i])
        year_contents = [x for x in contents if x.pub_date.date().year==year_nums[i]] 
        
        month = []
        month_nums = np.unique([x.pub_date.date().month for x in year_contents])
        for j in range(len(month_nums)):
            temp_month = {}
            temp_month.setdefault("num", month_nums[j])
            day_contents = [x for x in year_contents if x.pub_date.date().month==month_nums[j]]
            temp_month.setdefault("contents", day_contents)
            month.append(temp_month)
        temp_year.setdefault("month", month)
        
        year.append(temp_year)
 
    return render(request, "blog/timeline.html", {
        "year":year,
})


def split(request):
    blogs  = Article.objects.all()

    return render(request, "blog/page.html", {
        "blogs":blogs,
        "right": common_content(),     
        })