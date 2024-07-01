from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
# def my_view(request):
#     categories = Category.objects.all()
#     selected_category = request.GET.get('category')
#     posts = Post.objects.all()
#     return render(request, 'my_template.html', {'categories': categories, 'selected_category': selected_category, 'posts': posts})
