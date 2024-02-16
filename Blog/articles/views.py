from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from .models import Article
from .forms import LoginForm,UserRegistration,ArticleRegistrationForm,ArticleUpdateForm
from django.contrib.auth import logout
from django.shortcuts import redirect




from django.contrib.auth import authenticate,login
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


def user_login(request):
    if request.method == "POST":
        
        form = LoginForm(request.POST)
   

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'], password = cd['password'])

            if user is not None:
                login(request,user)
                return HttpResponse("you are authenticated")

            else:
                return HttpResponse("Invalid login")

    else:
        form = LoginForm()

    context = {
        'form': form
    }
    
    
    return render(request,'articles/login.html',context)



def user_register(request):
    if request.method == "POST":
        user_form = UserRegistration(request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])
             
            new_user.save()
            return render(request,'articles/register_done.html',)

    else:
        user_form = UserRegistration()
    context = {
        'user_form':  user_form
    }
    return render(request,'articles/register.html',context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request,'registration/logged_out.html')  
    

def add_article(request):
    if request.method == "POST":
        article_form = ArticleRegistrationForm(request.POST)
        # Handle form submission
        if article_form.is_valid():
            article = article_form.save(commit = False)
            article.author = request.user
            article.save()
            return redirect('article-list')
    else:
        article_form = ArticleRegistrationForm()
    
    
    
    context = {
        'article_form': article_form
    }
    
    return render(request, "articles/article_forms.html", context)




def update_article(request,slug):
    article = Article.objects.get(slug = slug)
    form =  ArticleUpdateForm(request.POST or None ,instance =article)
    if form.is_valid():
        form.save()
        return redirect('article-list')
    return render(request,"articles/update.html",{
        'form': form
    })