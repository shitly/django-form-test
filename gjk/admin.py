from django.contrib import admin

# Register your models here.
from gjk.models import Article

class ArticlesAdmin(admin.ModelAdmin):
    
    list_display = ["title", "column", "author", "sourcefrom"]


admin.site.register(Article, ArticlesAdmin)