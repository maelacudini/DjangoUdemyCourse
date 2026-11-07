from django.db import models
from django.utils.text import slugify

# https://docs.djangoproject.com/en/6.1/topics/db/models/

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
      
    class Meta:
        ordering = ["created_at"]
      
class Category(models.Model):
    caption = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Categories"

# An Author can be associated with many Posts, but a Post can only have one Author: this is a one-to-many relationship.
# A Post can be associated with many Categories, and a Category can be associated with many Posts: this is a many-to-many relationship.
class Post(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, help_text="Leave blank to auto-generate from title")
    title = models.CharField(max_length=100, unique=True)
    excerpt = models.TextField(max_length=200)
    image = models.ImageField(upload_to="post_images")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="posts")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")

    # overriding Django's built-in save() to automatically generate a unique slug based on the title if not provided
    # self is the current Post instance
    # *args collects extra positional arguments
    # **kwargs collects extra keyword arguments, such as force_insert=True or update_fields=["title"]
    def save(self, *args, **kwargs):
        if not self.slug:
            # slugify() converts the title into a URL-friendly string, [:100] is Python slicing, strip("-") removes hyphens from the beginning and end of the string
            base_slug = slugify(self.title)[:100].strip("-")
            slug = base_slug
            # if the base slug is already taken, we'll try appending -2: we start at 2 instead of 1 because the original slug has no suffix
            # e.g. hello-world, hello-world-2, hello-world-3
            counter = 2

            while Post.objects.filter(slug=slug).exists():
                # this is a Python f-string: it inserts the current value of counter into the string, e.g. -2
                suffix = f"-{counter}"
                slug = f"{base_slug[:100 - len(suffix)].rstrip('-')}{suffix}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
      
    class Meta:
        ordering = ["created_at"]