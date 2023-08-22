from django.urls import path
from .views import blog_title,blog_content
app_name = "blog"
urlpatterns = [
    path("",blog_title,name="blog_title"),
    path("<int:id>",blog_content)
]