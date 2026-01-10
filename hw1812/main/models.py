from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    cover = models.FileField(
        upload_to='covers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.title} — {self.author}"


class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.FileField(
        upload_to='avatars/',
        blank=True,
        null=True
    )

    books = models.ManyToManyField(
        Book,
        blank=True,
        related_name='readers'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"