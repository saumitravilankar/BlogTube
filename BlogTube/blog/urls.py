from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    # path("post_create/",views.PostCreateView.as_view(),name='post_create'),
    path("post_create_new/<int:pk>",views.PostCreateViewNew.as_view(),name='post_create_new'),
    # path("group_details/<int:pk>/post_list/",views.PostListView.as_view(),name="post_list"),
    path("post_details/<int:pk>",views.PostDetailView.as_view(),name="post_detail"),
    path("posts_published/",views.PostListView.as_view(),name='post_list'),
    path("post_edit/<int:pk>/<int:gpk>",views.PostUpdateView.as_view(),name="post_edit"),
    path("post_delete/<int:pk>",views.post_delete,name="post_delete"),

]