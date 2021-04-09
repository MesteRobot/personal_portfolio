from django.shortcuts import render, get_object_or_404
from .models import Blog
import math


def blog(request):
    # page_number = 1
    # blogs_per_page = 5
    # all_pages = math.ceil(Blog.objects.all().count()/5)
    # if request.GET.get("next") and page_number <= all_pages:
    #     page_number += 1
    # if request.GET.get("prev") and page_number > 1:
    #     page_number -= 1
    blogs = Blog.objects.order_by('-date_created')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html", {'blog': blog})
