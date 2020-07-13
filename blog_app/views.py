from django.shortcuts import render
from .models import BlogFrame
from django.shortcuts import render, get_object_or_404

# Create your views here.

def main(request):
    blog=BlogFrame.objects

    return render(request,'main.html', {'blog':blog })

def detail(request,blog_id):
    blog_detail = get_object_or_404(BlogFrame, pk=blog_id)
    return render(request,'detail.html',{'blog_detail':blog_detail})