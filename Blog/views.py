from django.shortcuts import render

def index(request):

    return render(request,'Blog/index.html',locals())


def detail(request,blog_id):

    return render(request,'templates/detail.html',locals())
