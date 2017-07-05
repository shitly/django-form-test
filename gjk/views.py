import re
from datetime import datetime, date, time, timedelta
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from news.models import Categary
from news.utils import all_article

from gjk.forms import SearchForm
# Create your views here.

@login_required
def tag_articles(request):
    
    return render(request, "gjk/search_chart.html", {

})

@login_required
def manager(request):
    return render(request, "new_chart.html", {
    "chart_disc": "默认初始天数的文章情况概览表",
})

def show(request):
    if request.method == 'GET':
        form = SearchForm(initial={'title_word': "."})
        return render(request, 'gjk/search_chart.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = SearchForm(request.POST)
        # 探究搜索关键词为空的内容// 搜素全部为 .
        if form.is_valid():

            tag = form.cleaned_data['tag']
            start_date = form.cleaned_data['serach_start']
            end_date = form.cleaned_data['serach_end']
            word = form.cleaned_data['title_word']
            temp_res = all_article()[tag.id]
            result0 = [x for x in temp_res if x.pub_date.date() > start_date and x.pub_date.date() < end_date]
            result = []
            for x in result0:
                if re.match(".*" + word + ".*", x.title):
                    result.append(x)
            return render(request, "gjk/search_chart.html", {
                'form': form,
                'result': result,
            })
    return render(request, 'gjk/search_chart.html', {'form': form})
    

## 必须登录才能看到
@login_required
def homepage(request):
    return render(request, "post_article.html", {

})

def charts(request):
    return render(request, "chart.html", {
        "chart_disc": "最近一月发表文章状况图",
    })


# 写入
def test(request):
    if request.method == 'GET':

        return render(request, "post_article.html", {

        })
    if request.method == 'POST':
        cate = request.POST["tag"]

        author = request.POST["author"]
        source_from=request.POST["source_from"]
        title=request.POST["title"]
        img=request.POST["img"]
        abstract=request.POST["abstract"]
        content=request.POST["content"]
        c = Categary.objects.get(id=int(cate))
        slug_url = c.url

        from gjk.models import Article
        Article.objects.create(
            title=title, 
            column=c,
            img=img,
            abstract=abstract,
            content=content, 
            author=author, 
            sourcefrom=source_from, 
            slug_url= slug_url,
        )

        return HttpResponse("写入完成")
    else:
        return HttpResponse("??????")



from .utils import history_tables
def data_json(request):
    ## 耗时耗力的设计// 舍弃
    days = 30
    import datetime as dt
    now = dt.datetime.now()

    xlables = [(now-dt.timedelta(days=days-i-1)).date() for i in range(days)]

    n = len(all_article())
    cates = Categary.objects.all()
    data = []
    legend = []
    for i in [i+1 for i in range(n-1)]:
        temp_dir = {}

        name = cates[i-1].categary
        temp_dir.setdefault("name", name)
        temp_dir.setdefault("type", "line")
        temp_dir.setdefault("stack", "总量")
        result_data = []
        for day_num in range(days-1):
            y = len([x for x in all_article()[i] if xlables[day_num+1] > x.pub_date.date() >= xlables[day_num]])
            result_data.append(y)
        temp_dir.setdefault("data", result_data)

        legend.append(name)
        data.append(temp_dir)

    return JsonResponse({
        "xlables": xlables[:days-1],
        "data": data,
        "legend": legend,
    })


def data_dict(request):
    
    return JsonResponse(history_tables())



def chart_json_start_end(start_date, end_date):

    res = history_tables()

    '''
    date_start = date(2017, 3 ,3)
    date_end = datetime.now().date()
    dates = [date_start + timedelta(days=i) for i in range(150)
         if date_start + timedelta(days=i) < date_end]
    
    for x in res.keys():
        
        for _date in dates:
            for y in res[x].keys():
                if _date not in res[x]["rq"]:
                    res[x]["rq"].append(_date)
                    res[x]["num"].append(0)
    '''
    xlables = []
    for x in range(200):
        temp_date = start_date + timedelta(days=x)
        if temp_date < end_date:
            xlables.append(temp_date)
        else:
            break

    legend = [x for x in res.keys()]

    data = []
    for x in res.keys():
        t_dir = {}
        t_dir.setdefault("name", x)
        t_dir.setdefault("type", "line")
        t_dir.setdefault("stack", "总量")
        result_data = []
            
        for _date in xlables:
            if _date in res[x]["rq"]:
                locate = res[x]["rq"].index(_date)
                result_data.append(res[x]["num"][locate])
            else:
                result_data.append(0)
        t_dir.setdefault("data", result_data)
        data.append(t_dir)
    
    return xlables, data, legend
 
    

def json(request):
    # 默认 5-1 到7.2 的 
    xlables, data, legend = chart_json_start_end(date(2017,5,1), date(2017,7,2))
    
    return JsonResponse({
        "xlables": xlables,
        "data": data,
        "legend": legend,
    })


from .forms import TwoMenberDateForm
def zxt(request):
    if request.method == 'GET':
        form = TwoMenberDateForm()
        return render(request, 'gjk/search_zxt.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = TwoMenberDateForm(request.POST)
        # 探究搜索关键词为空的内容// 搜素全部为 .
        
        if form.is_valid():
            start_date = form.cleaned_data['serach_start']
            end_date = form.cleaned_data['serach_end']

            # 默认 5-1 到7.2 的 
            xlables, data, legend = chart_json_start_end(start_date, end_date)
            import json
            return render(request, "gjk/search_zxt.html",{
                        "xlables": xlables,
                        "data": data,
                        "legend": legend,
                        "desc": "时间段内的图像",
        })

        return render(request, 'gjk/search_zxt.html', {
            'form': form,
        })


def json2(request, date1, date2):
    try:
        xlables, data, legend = chart_json_start_end(date1, date2)
    except:
        return HttpResponse("时间设置有误")
    return JsonResponse({
        "xlables": xlables,
        "data": data,
        "legend": legend,
    })


from .forms import ContactForm
def send_email(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'gjk/send_email.html', {
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
                'm13429888211@163.com', 
                ["m13429888211@163.com", ], #"2970090120@qq.com"
        )
        
        msg.content_subtype = "html"
        
        # 添加附件（可选）
        # msg.attach_file('F:\\TEST\\msg\\tests.pdf')
        
        # 发送
        msg.send()

        return HttpResponse("发送成功！")
    return render(request, 'gjk/send_email.html', {
            'form': form,
        })

def test_JSdate(request):
    return render(request, "date.html", {

})

