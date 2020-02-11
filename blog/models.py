from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.tag


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.CharField(max_length=60)
    text = models.TextField()

    def __str__(self):
        return self.text


