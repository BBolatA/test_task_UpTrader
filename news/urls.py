from django.urls import path
from django.views.generic import TemplateView

app_name = "news"

urlpatterns = [
    path("", TemplateView.as_view(template_name="news/list.html"), name="list"),
    path("categories/", TemplateView.as_view(template_name="news/categories.html"), name="categories"),
    path("categories/it", TemplateView.as_view(template_name="news/it.html"), name="cat-it"),
]
