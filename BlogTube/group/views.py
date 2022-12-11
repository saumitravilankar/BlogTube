from django.shortcuts import render
from .models import Group,GroupMember
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from django.contrib import messages

from django.db import IntegrityError

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView,DetailView,CreateView,RedirectView


# Create your views here.
class GroupListView(ListView):
    
    context_object_name = 'group_list'
    model = Group
    template_name = 'group/group_list.html'
    extra_context = {'title': 'Groups'}

class GroupDetailView(DetailView):

    model = Group
    extra_context = {'title': 'Group Details'}

class GroupCreateView(LoginRequiredMixin,CreateView):
    # login_required = True
    # login_url = "login"
    # redirect_field_name = "group:group_create"
    model = Group
    fields = ('name','description')
    success_url = reverse_lazy('group:group_list')
    extra_context = {'title': 'Create Group'}

class GroupJoin(RedirectView):

    # login_required = True
    # redirect_field_name = 'group/group_detail'
    # pattern_name = 'group:group_detail'
    
    # def get_redirect_url(self, *args **kwargs):
    #     GroupMember.objects.create(profile=self.request.user.username,group=self.group)
    #     return reversed('group:group_detail',kwargs={'pk':self.pk})
        def get_redirect_url(self, *args, **kwargs):
            group = Group.objects.filter(id=self.kwargs['pk']).first()
            GroupMember.objects.create(profile=self.request.user.profile,group=group)
            return reverse("group:group_detail",kwargs={"pk": self.kwargs['pk']})
    
    # def get(self, request, *args,**kwargs):
    #     group = get_object_or_404(Group,id=self.kwargs['pk'])
    #     GroupMember.objects.create(profile=self.request.user.profile,group=group)
    #     return super().get(request, *args, **kwargs)

class GroupJoinInvite(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
         return reverse('group:group_detail',kwargs={'pk':self.kwargs['pk']})

class GroupLeave(RedirectView):

    # pattern_name = 'group:group_details'

    # Here i am using profile_id and group_id to select exact GroupMember object for deleting.
    # Came to know about profile_id and group_id from python manage.py shell --> GroupMember.objects.values()

    def get_redirect_url(self, *args, **kwargs):
        Membership_to_delete = GroupMember.objects.get(profile_id=self.kwargs['profile_id'],group_id=self.kwargs['group_id'])
        Membership_to_delete.delete()
        return reverse("group:group_detail",kwargs={"pk": self.kwargs['group_id']})