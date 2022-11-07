from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from colorfield.fields import ColorField

from . import storage_backend

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=120, blank=True)
    comment = models.TextField(blank=True)
    color = ColorField(default="#FFFFFF")
    image = models.ImageField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    email_template_material = models.TextField(blank=True)
    email_template_money_limited = models.TextField(blank=True)
    email_template_money_unlimited = models.TextField(blank=True)

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
    image = models.ImageField(blank=True, null=True)

    wish_type = models.CharField(max_length=10, choices=WISH_TYPES)
    ammount = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    link = models.TextField(blank=True)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="wishes")

    gifted = models.BooleanField(default=False)

    order = models.IntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def percentage(self):
        if self.wish_type == self.MONEY_UNLIMITED:
            return None
        if self.gifts.exists():
            if self.count:
                gift_sum = self.gifts.aggregate(Sum("count"))["count__sum"]
                return gift_sum / self.count * 100
            elif self.ammount:
                gift_sum = self.gifts.aggregate(Sum("ammount"))["ammount__sum"]
                return gift_sum / self.ammount * 100
        else:
            return 0

    class Meta:
        ordering = ["order", "created"]
        verbose_name_plural = "Wishes"


class Gift(models.Model):
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, related_name="gifts")

    ammount = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)

    name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.TextField(blank=True)
    phone =  models.CharField(max_length=60, blank=True)

    comment = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.wish.title} from {self.name}"

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "Gifts"
