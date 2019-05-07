from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    contenu = models.TextField()
    comment = models.TextField()
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.titre

    def __unicode__(self):
        return self.titre

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        pic = Image.open(self.photo.path)

        if pic.height > 4000 or pic.width > 4000:
            output_size = (4000, 4000)
            pic.thumbnail(output_size)
            pic.save(self.photo.path)

