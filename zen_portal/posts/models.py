from django.conf import settings
from django.db import models


# Create your models here.


class Post(models.Model):
    text = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    average = models.FloatField(default=0.0)

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=255)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
