from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render
from .models import Post

# logic executed for different urls, and Http methods
# can be a class or a function
# classes and functions contain code that handles the request and returns a response
# views load an prepare data, run any business logic, and return a response
# https://docs.djangoproject.com/en/6.1/topics/http/views/
# https://docs.djangoproject.com/en/6.1/topics/class-based-views/intro/


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"

    # read https://coddy.tech/learn/it/django/classbased_views/filtering_with_get_queryset
    def get_queryset(self):
        posts = Post.objects.prefetch_related("categories")
        categories = self.request.GET.get("categories", "").strip()

        if categories:
            posts = posts.filter(categories__caption__iexact=categories)

        return posts.distinct()

class PostView(DetailView):
    model = Post
    template_name = "blog/post.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

class ContactView(TemplateView):
    template_name = "blog/contact.html"
