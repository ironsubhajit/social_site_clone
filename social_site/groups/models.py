from django.db import models

from django.contrib.auth import get_user_model

from django import template


User = get_user_model()
register = template.Library()


class Group(models.Model):
    pass


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='membership', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")