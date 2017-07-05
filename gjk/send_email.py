import os

###
from os.path import dirname, abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
import sys
sys.path.insert(0, PROJECT_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "minicms.settings"

import django
django.setup()


from django.core import mail
from django.core.mail import send_mail


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
 
 
from_email = settings.DEFAULT_FROM_EMAIL
# subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
msg = EmailMultiAlternatives(
        "markdown测试粗体", 
       "<h1>测试<h1></br><strong>cuti</strong>", 
        'm13429888211@163.com', 
        ["m13429888211@163.com"],
)
 
msg.content_subtype = "html"
 
# 添加附件（可选）
msg.attach_file('F:\\TEST\\msg\\tests.pdf')
 
# 发送
msg.send()