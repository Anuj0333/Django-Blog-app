from django.urls import path
from .views import PostListView,PostDetailView,PostCreatelView,PostUpdateView,PostDeletelView,UserPostListView
from . import views

urlpatterns = [
   # path("", views.home,name='blog-home'),
    path("",PostListView.as_view(template_name="blog/home.html"),name='blog-home'),
    path("user/<str:username>", UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreatelView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeletelView.as_view(), name='post-delete'),
    path("about/",views.about, name='blog-about'),

]