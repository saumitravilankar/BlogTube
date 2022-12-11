from django.db import models
from user.models import Profile
from django.utils import timezone
# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=5000)

    # This field will be filled through GroupMember.
    profile = models.ManyToManyField(Profile,through='GroupMember')

    @property
    def postlist(self):
        post_list = self.post_set.filter(created_on__lte=timezone.now()).order_by('-created_on')
        return post_list
    
    @property
    def postcount(self):
        posts = self.post_set.all()
        post_count = len([post for post in posts])
        return post_count

    def __str__(self) -> str:
        return self.name

class GroupMember(models.Model):
    profile = models.ForeignKey(Profile,related_name='members',on_delete=models.CASCADE)
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.profile.user.username

    class Meta:
        unique_together = ('profile','group')

