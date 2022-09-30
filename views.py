from django.shortcuts import render
from . models import Posts, Audio, Videos, Images

# Create your views here.

def home(request):
    return render(request, 'jassong/home.html')


def resources(request):
    images = Images.objects.all()
    audious = Audio.objects.all()
    videos = Videos.objects.all()
    context = {"images": images, "audious": audious, "videos": videos}
    return render(request, 'jassong/resources.html', context)

def newsFeed(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'jassong/post.html', context)


def donation(request):
    return render(request, 'jassong/donation.html')


def mosque(request):
    return render(request, 'jassong/mosque.html')


def about(request):
    return render(request, 'jassong/about.html')

def contact(request):
    return render(request, 'jassong/contact.html')

