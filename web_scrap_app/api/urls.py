from django.urls import path, include
from . import views

urlpatterns = [
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("blog/<int:id>/", views.BlogDetailView.as_view(), name="blog_detail"),
]
