from django.db import models
import uuid
from django.utils import timezone

class Item(models.Model):
    identification = models.CharField(max_length=100, unique=True, editable=False)
    name = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='assets/images/items/', null=True, blank=True)
    details = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    media = models.ManyToManyField('Media', related_name='items')
    is_discounted = models.BooleanField(default=False)
    percentage = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ItemsModel'
        verbose_name = 'Item'

    def save(self, *args, **kwargs):
        if not self.identification:
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            unique_id = str(uuid.uuid4().int)[:4]
            self.identification = f"{timestamp}-{unique_id}-{self.name}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}-{self.identification}-{self.date_created}"

class Media(models.Model):
    pass

class Image(models.Model):
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='assets/images/items/')

class Video(models.Model):
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    video = models.FileField(upload_to='assets/videos/items/')

class Specification(models.Model):
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    files = models.FileField(upload_to='assets/files/items/')