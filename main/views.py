from django.shortcuts import redirect, render
from .models import *
from .forms import ContactForm,CommentBlogForm
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .forms import CommentBlogForm 
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views.generic import DetailView

class intro (generic.ListView):
    model = Blog
    template_name = "main/intro.html"

class videos (generic.ListView):
    model = Blog
    template_name = "main/videos.html"

class gallery (generic.ListView):
    model = Blog
    template_name = "main/gallery.html"   

class about_us (generic.ListView):
    model = Blog
    template_name = "main/about.html"

   
class category(generic.ListView):
    model = Category
    template_name = "main/services.html"
    paginate_by = 3
    paginate_by2 = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_entries'] = self.pagination(self.request)
        return context

    def pagination(self, request):
        all_category_entries = Category.objects.all()
        paginator = Paginator(all_category_entries, self.paginate_by2)
        page = request.GET.get('page')
        category_entries = paginator.get_page(page)
        return category_entries
    
def category_detail (request, slug,*args, **kwargs):
   
    all_blog_entries = Blog.objects.all().order_by('-post_date')
    blog_paginator = Paginator(all_blog_entries, 6)
    blog_page = request.GET.get('blog_page')
    blog_entries = blog_paginator.get_page(blog_page)
 
    category_entries = Category.objects.all()
    category = Category.objects.get(slug=slug)
    post = Blog.objects.filter(category=category)
    post_count = post.count()
    all_categories = Category.objects.all()[:10]
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]
    
    context = {
        'category':category,
        'all_categories': all_categories,
        'category_entries':category_entries,
        'blog_entries': blog_entries,
        'post': post,
  
        'post_count': post_count,
        'all_blogs':all_blogs
        
    }
    #view count

    category.views += 1
    category.save()

    return render(request, "main/category_detail.html", context)


class blog_home(generic.ListView):
    model = Blog
    template_name = "main/blog_home.html"
    context_object_name = 'object_list'


class blog(generic.ListView):
    template_name = "main/blog.html"
    paginate_by = 3
    paginate_by2 = 6

    def get(self, request, *args, **kwargs):
        # Fetch blog entries
        all_blog_entries = Blog.objects.all().order_by('-post_date')
        blog_paginator = Paginator(all_blog_entries, self.paginate_by)
        blog_page = request.GET.get('blog_page')
        blog_entries = blog_paginator.get_page(blog_page)

        # Fetch category entries
        all_category_entries = Category.objects.all()
        category_paginator = Paginator(all_category_entries, self.paginate_by2)
        category_page = request.GET.get('category_page')
        category_entries = category_paginator.get_page(category_page)

        context = {
            'blog_entries': blog_entries,
            'category_entries': category_entries,
        }

        return render(request, self.template_name, context)

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_blogs'] = Blog.objects.all().order_by('-post_date')[:10]
        context['form'] = CommentBlogForm()
        context['all_comments'] = BlogComment.objects.filter(blog=self.object)
        context['blog_entries'] = Blog.objects.all().order_by('-post_date')[:6]
        context['category_entries'] = Category.objects.all()

        # Increment view count
        self.object.views += 1
        self.object.save()

        return context
     
def blog_detail(request, slug):
    all_blog_entries = Blog.objects.all().order_by('-post_date')
    blog_paginator = Paginator(all_blog_entries, 6)
    blog_page = request.GET.get('blog_page')
    blog_entries = blog_paginator.get_page(blog_page)

    blog = get_object_or_404(Blog, slug=slug)
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]
    all_comments = BlogComment.objects.filter(blog=blog)

    if request.method == 'POST':
        form = CommentBlogForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            form = CommentBlogForm()  # Reset the form after saving
        else:
            print(form.errors)  # Check for form validation errors
    else:
        form = CommentBlogForm()

    category_entries = Category.objects.all()

    context = {
        'blog': blog,
        'all_blogs': all_blogs,
        'form': form,
        'all_comments': all_comments,
        'blog_entries': blog_entries,
        'category_entries': category_entries,
    }

    # Increment view count
    blog.views += 1
    blog.save()

    return render(request, "main/blog_detail.html", context)
    



class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "main/contact_us.html"
    success_url = "/"
    success_message = "Your query has been submited successfully, we will contact you soon."
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")
        return redirect('home')

