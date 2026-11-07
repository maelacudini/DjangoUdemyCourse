from django.urls import path
from blog.views import HomeView, PostView, ContactView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts/<slug:slug>", PostView.as_view(), name="post"),
    path("contact", ContactView.as_view(), name="contact"),
]