from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    date_created = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def slice(self):
        return ' '.join(self.content.split(' ')[:3]) + '...'


class Photo(models.Model):
    image = models.ImageField(default='image.jpg', blank=True)
    post = models.ForeignKey('app.Post', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body
