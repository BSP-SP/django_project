from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author' :'Bineesh s p',
        'title' : 'Blog post 1',
        'content':'First post content',
        'date_posted' : 'August 18 ,2018'
    },
    {
        'author' :'Binoy s p',
        'title' : 'Blog post 2',
        'content':'Second post content',
        'date_posted' : 'August 25 ,2018'
    }
]



# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{ 'title':'About' })

