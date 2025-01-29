from rest_framework import serializers
from quote import models

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'title')

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quote
        fields = ('id', 'image', 'text', 'author', 'tags')

    def create(self, validated_data):
        image = 'default.jpg'
        author = 'Anonymous'
        if validated_data.get('image') is not None:
            image = validated_data.get('image')
        if validated_data.get('author') is not None:
            author = validated_data.get('author')
        text = validated_data.get('text')
        tags = validated_data.get('tags')
        # tag_objs = []
        # for tag in tags:
        #     t = dict(tag).get('title')
        #     tag_objs.append(models.Tag.objects.get(title=t))
        # print(tag_objs)
        quote = models.Quote(text=text, image=image, author=author)
        quote.save()
        quote.tags.set(tags)
        return quote