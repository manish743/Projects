from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, template_name="blog/index.html", context={'blogs' : blogs})

def blog_detail(request, pk):
    blog = BlogPost.objects.get(pk = pk)
    return render(request, template_name="blog/blog_detail.html", context={'blog' : blog})

def edit_blog(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, template_name="blog/edit.html", context={'form' : form})

def delete_blog(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')
    return render(request, template_name="blog/delete.html", context={'blog' : blog})