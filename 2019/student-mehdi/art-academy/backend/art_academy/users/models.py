from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField(default=0)
    price_per_hour = models.FloatField(default=0.0)
    hour = models.FloatField(default=0.0)
    payment_type = models.ForeignKey('PaymentType', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Payment at {self.date}'



class PaymentType(models.Model):
    payment_type = models.CharField(max_length=20, default='Cash')

    def __str__(self):
        return f'{self.payment_type}'
