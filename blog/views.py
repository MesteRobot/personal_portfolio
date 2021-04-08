from django.shortcuts import render
from .models import Blog
import math


def blogs(request):
    page_number = 1
    blogs_per_page = 5
    all_pages = math.ceil(Blog.objects.all().count()/5)
    if request.GET.get("next") and page_number <= all_pages:
        page_number += 1
    if request.GET.get("prev") and page_number > 1:
        page_number -= 1
    blogs = Blog.objects.order_by('-date_created')[(page_number - 1) * blogs_per_page:page_number * blogs_per_page]
    return render(request, 'blog/blogs.html', {'blogs': blogs, 'page_number': page_number, 'all_pages': all_pages})


