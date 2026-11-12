from django.urls import path
from . import views

# urlpatterns = [
#     path("home",views.home_page),
#     path("python",views.python_intro),
#     path("django",views.django_basics),
# ]


# urlpatterns = [
#     path("", views.home_page),
#     # path("<int:blog>/", views.for_int),
#     # path("<str:blog>/", views.for_str),,
#     path("", views.blog_post),
#     path("<slug:blog>/", views.blog_post)  
# ]





urlpatterns = [
    path("", views.home_page,name = "home"),
    path("all-posts/", views.all_posts,name = "blogpage"),
    path("all-posts/<slug:blog>/", views.blog_posts,name = "allposts")
    ]    