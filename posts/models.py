from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # Relacion
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey( 'users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField( upload_to='posts/photos' )
    created = models.DateField(auto_now_add=False)
    modified = models.DateField(auto_now=False)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)