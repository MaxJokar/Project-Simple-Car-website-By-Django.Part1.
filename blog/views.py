from django.shortcuts import render
from .models import Post


def home(request):
    data = Post.objects.all() # we wanna collect all the  data
    return render(request, "index.html",{"posts":data})


def electric(request , slug):
    # we wanna collect specific/one item /field name from  data
    data = Post.objects.get(slug=slug)
    return render(request, "electric.html",{"post":data})




def aboutUs(request):

    return render(request, "aboutUs.html",{})

