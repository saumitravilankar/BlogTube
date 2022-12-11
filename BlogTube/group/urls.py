from django.urls import path
from . import views

app_name='group'

urlpatterns = [
    path("group_detail/<int:pk>",views.GroupDetailView.as_view(),name='group_detail'),
    path("group_list/",views.GroupListView.as_view(),name='group_list'),
    path("group_create/",views.GroupCreateView.as_view(),name='group_create'),
    path("group_join/<int:pk>",views.GroupJoin.as_view(),name='group_join'),
    path("group_join_invite/<int:pk>", views.GroupJoinInvite.as_view(), name="group_join_invite"),
    path("group_leave/<int:profile_id>/<int:group_id>",views.GroupLeave.as_view(),name='group_leave'),
]
