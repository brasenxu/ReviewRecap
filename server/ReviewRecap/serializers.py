from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "url", "last_update",
                  "keyword1", "keyword1_rating", "keyword1_freq",
                  "keyword2", "keyword2_rating", "keyword2_freq",
                  "keyword3", "keyword3_rating", "keyword3_freq",
                  "keyword4", "keyword4_rating", "keyword4_freq",
                  "keyword5", "keyword5_rating", "keyword5_freq",)
