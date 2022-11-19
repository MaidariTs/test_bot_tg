from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Users(models.Model):
    user_id = models.IntegerField(null=False)
    join_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )


class Records(models.Model):
    user_id = models.ForeignKey(
        Users,
        null=False,
        related_name='record'
    )
    operaion = models.BooleanField(null=False)
    value = models.DecimalField(null=False)
    date = models.DateTimeField(auto_now_add=True)
