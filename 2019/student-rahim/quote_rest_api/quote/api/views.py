from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import serializers
from quote import models



class ListCreateQuote(generics.ListCreateAPIView):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer


class RetrieveUpdateDestroyQuote(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer


class ListCreateTag(generics.ListCreateAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer

class RetrieveUpdateDestroyTag(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


# for version 2 of the api
class QuoteViewSet(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

    @detail_route(methods=['get'])
    def tags(self, request, pk=None):
        quote = self.get_object()
        serializer = serializers.TagSerializer(
            quote.tags.all(), many=True)
        return Response(serializer.data)

class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer