# Django class-based views: `get()`, `get_queryset()`, and `get_context_data()`

These methods do different jobs:

| Method | What it controls | Commonly used with |
|---|---|---|
| `get()` | Handles an HTTP GET request and returns the response | Any class-based view |
| `get_queryset()` | Chooses which model objects the view can use | `ListView`, `DetailView` |
| `get_context_data()` | Adds values that the template can use | `TemplateView`, `ListView`, `DetailView` |

## `get()`: handle the request

`get()` runs when the view receives a GET request. It is responsible for returning a response. Override it when you need custom request/response behavior.

Generic views already implement `get()`. For example, `TemplateView` handles the request, builds the template context, and renders the template. You usually do not need to override `get()` just to pass data to a template.

If you override `get()`, you take responsibility for returning the response and may bypass the generic view's normal flow.

## `get_queryset()`: choose the objects

`get_queryset()` returns the queryset of model objects a view should work with. It is provided by model-based views such as `ListView` and `DetailView`; `TemplateView` does not use it.

Use it to filter or optimize the objects shown by the page. For example, a post list can filter by a category from the URL query string:

```python
from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.prefetch_related("categories")
        tag = self.request.GET.get("tag", "").strip()

        if tag:
            posts = posts.filter(categories__caption__iexact=tag)

        return posts.distinct()
```

For example, `/?tag=django` displays posts with a matching category. `prefetch_related("categories")` fetches the related categories efficiently when the template displays them for multiple posts. `distinct()` avoids duplicate posts if a relationship filter matches more than once.

`DetailView` also uses `get_queryset()` to determine which objects can be looked up. Its default behavior finds one object by the URL's primary key or slug; overriding the method lets you narrow that lookup.

## `get_context_data()`: add template values

`get_context_data()` builds the context dictionary passed to the template. Override it when the template needs additional data beyond the view's main object or queryset. Always call `super()` to keep the context supplied by the generic view.

For example, add all categories to the post list page:

```python
from .models import Category


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categories"] = Category.objects.all()
    return context
```

In the template, those values are available as `categories`. `ListView` also supplies the object list as `object_list`; in the example above, `context_object_name = "posts"` makes it available as `posts`.

## Choosing the right method

- Need to customize how a request is handled or what response is returned? Use `get()`.
- Need to choose, filter, or optimize model objects? Use `get_queryset()` on a view that supports it, such as `ListView` or `DetailView`.
- Need extra values for the template? Use `get_context_data()`.

For a page that lists posts, `ListView` with `get_queryset()` is usually a better fit than overriding `get()` in `TemplateView`. For a page that displays one post, use `DetailView` and customize its queryset or context only when needed.

### Extra resources: https://medium.com/@hassanraza/when-to-use-get-get-queryset-get-context-data-in-django-952df6be036a