from base64 import b64decode

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view(["GET"])
def get_product(request, b64):

    url = b64decode(b64).decode("utf-8")
    name = url.split("/")[0] + url.split("/")[3]

    try:
        product = Product.objects.get(pk=name)
    except Product.DoesNotExist:
        # Replace this part with data parser
        print(f"https://amazon.{url.replace('/dp/', '/product-reviews/')}/pageNumber=")
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = dict(ProductSerializer(product).data)
    return Response({
        "id": data["id"],
        "data": [
            {"keyword": data["keyword1"],
             "rating": data["keyword1_rating"],
             "freq": data["keyword1_freq"]},
            {"keyword": data["keyword2"],
             "rating": data["keyword2_rating"],
             "freq": data["keyword2_freq"]},
            {"keyword": data["keyword3"],
             "rating": data["keyword3_rating"],
             "freq": data["keyword3_freq"]},
            {"keyword": data["keyword4"],
             "rating": data["keyword4_rating"],
             "freq": data["keyword4_freq"]},
            {"keyword": data["keyword5"],
             "rating": data["keyword5_rating"],
             "freq": data["keyword5_freq"]}
        ]
    })
