from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from group.models import Group
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    # This user field will not be in form it will be filled with request.user during form validation
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)

    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("group:group_detail", kwargs={"pk": self.group.pk})
    

    def __str__(self) -> str:
        return self.title


