from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.db import models

from colorfield.fields import ColorField


def generate_auth():
    return  get_random_string(length=6, allowed_chars='ABCDEFGHJKLMNPQRSTUVWXYZ23456789')

def generate_url():
    for _ in range(20):
        url = get_random_string(length=7, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        if not Collection.objects.filter(url=url).exists():
            return url
    raise ValueError('Too many attempts to generate the url')

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=120, blank=True)
    comment = models.TextField(blank=True)
    color = ColorField(default="#FFFFFF")
    # image = models.ImageField(null=True)

    auth = models.CharField(max_length=10, default=generate_auth)
    auth_enabled = models.BooleanField(default=True)
    url = models.CharField(max_length=20, default=generate_url, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "Collections"

class Wish(models.Model):
    MONEY_UNLIMITED = "MUL"
    MONEY_LIMITED = "ML"
    MATERIAL = "MAT"
    WISH_TYPES = (
        (MONEY_UNLIMITED, 'Money unlimited gift'),
        (MONEY_LIMITED, 'Money gift'),
        (MATERIAL, 'Material gift'),
    )

    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=120, blank=True)
    comment = models.TextField(blank=True)
    color = ColorField(default="#FFFFFF")
    # image = models.ImageField(null=True)

    wish_type = models.CharField(max_length=10, choices=WISH_TYPES)
    ammount = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    link = models.TextField(blank=True)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="wishes")

    order = models.IntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["order", "created"]
        verbose_name_plural = "Wishes"
