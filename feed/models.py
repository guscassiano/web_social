from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    message = models.TextField(max_length=500, verbose_name='Mensagem')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Postado em')

    @property
    def total_likes(self):
        return self.like_set.count()

    class Meta:
        ordering = ['-created_at']
        verbose_name='Post'

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')