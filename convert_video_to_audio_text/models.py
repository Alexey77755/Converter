from django.db import models
from django.contrib.auth.models import User


class Audio(models.Model):
    text = models.TextField()

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text
