from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    description = models.TextField(max_length=400, blank=True, null=True, verbose_name='Biografia')
    photo = models.ImageField(upload_to='perfil/', blank=True, null=True, verbose_name='Imagem de perfil')

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')
