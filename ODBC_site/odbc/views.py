from django.shortcuts import render

# Create your views here.

def index(request):
    
    style_name = 'index'
    
    return render(request, 'odbc/index.html', {'style_name' : style_name})


def about(request):

    style_name = 'about'
    
    return render(request, 'odbc/about.html', {'style_name' : style_name})

def announcements(request):

    style_name = 'announcements'
    
    return render(request, 'odbc/announcements-news.html', {'style_name' : style_name})
