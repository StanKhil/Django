from django.db import models

# Create your models here.

class Prediction(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Poem(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="poems")
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="poems")

    def __str__(self):
        return self.title
