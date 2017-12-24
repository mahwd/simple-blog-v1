from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from random import randint
from ckeditor.fields import RichTextField


class User(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")
    user_name = models.CharField(max_length=20, verbose_name="surname")
    email = models.CharField(max_length=20, verbose_name="email")


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Başlıq")
    content = RichTextField(verbose_name="Mətn")
    publish_date = models.DateField(verbose_name="Tarix", default=timezone.now)
    image = models.ImageField(null=True, blank=True, verbose_name='Şəkil')
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('insta_app:post_details', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('insta_app:post_delete', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('insta_app:post_update', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = Post._get_unique_slug(self)
        super(Post, self).save(*args, **kwargs)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        while Post.objects.filter(slug=slug).exists():
            slug = "{}-{}".format(slug, randint(0, 1298))
        return slug

    class Meta:
        ordering = ["-publish_date", "-id"]
