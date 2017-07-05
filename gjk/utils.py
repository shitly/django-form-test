import pymysql
from minicms.settings import MPP_ODS_CONFIG
from news.models import Categary

def history_tables():

    tables = ["news_focusarticle", "news_policyarticle", "news_southsafeseenarticle", 
    "news_lawarticle", "news_talentsarticle", "news_techarticle", "news_popularscience"]
    conn = pymysql.connect(**MPP_ODS_CONFIG)
    # import pandas as pd
    # import numpy as np 
    cates = [x.categary for x in Categary.objects.all()]
    temp_dir = {}
    index = 0
    for table in tables:
        cursor = conn.cursor()
        cursor.execute('''select date(pub_date),count(id) from '''+ table +''' group by date(pub_date);''')
        # temp_dir.setdefault(cates[index], pd.DataFrame(np.array(cursor.fetchall()), columns=["rq", "num"]))
        
        temp, rq, num = {}, [], []
        for x in cursor.fetchall():
            rq.append(x[0])
            num.append(x[1])
        temp.setdefault("rq", rq)
        temp.setdefault("num", num)
        
        temp_dir.setdefault(cates[index], temp)
        cursor.close()
        index += 1
    conn.close()
    return temp_dir


from django.shortcuts import render
from django.core.mail import send_mail
def send_msg(request):
    from .forms import ContactForm
    if request.method == 'GET':
        form = ContactForm()
        return render(request, "msg.html", {"form": form})

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
        else:
            return HttpResponseRedirect('/gaojianku/admin/msg/')