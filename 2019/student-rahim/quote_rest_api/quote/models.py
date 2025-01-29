from django.db import models


class Tag(models.Model):
    title = models.SlugField(max_length=50)
   
    def __str__(self):
        return self.title


class Quote(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='quote_pics')
    text = models.TextField()
    author = models.CharField(max_length=100, default='Anonymous')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'Quote from {self.author}'
