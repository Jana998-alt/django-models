from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model


# Create your models here.

class Snack(models.Model):
    name = models.TextField(max_length=64)
    purchaser = models.ForeignKey(to = get_user_model(),on_delete=(models.CASCADE), default= 1)
    description = models.TextField(max_length=256)

    def __str__(self) -> str:
        return self.name
        