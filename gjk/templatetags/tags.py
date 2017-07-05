from django import template

register = template.Library()
from django.template.defaultfilters import stringfilter


@register.filter(name="cate")
def cate(value):
    urls = ["focus_detail", "policy_detail", "law_detail", 
    "talents_detail", "tech_detail", "popular_detail"]
    cates = ["安全热点", "管理政策", "安全法制", "人才培养", "前沿技术", "热点专题"]

    if value.slug_url in urls:
        locate = urls.index(value.slug_url)
        return cates[locate]
    else:
        return "南方安全热点"