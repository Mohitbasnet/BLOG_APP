from django.shortcuts import render,get_object_or_404
from .models import Article
# Create your views here.



def article_list(request):
    article_list = Article.objects.all().order_by('-published')


    
    context = {
        'article_list': article_list
    }
    return render(request,"article.html",context)

def article_detail(request,slug):

    article = get_object_or_404(Article, slug = slug)
    context = {
        'article':article
    }
    return render(request,'details.html', context)