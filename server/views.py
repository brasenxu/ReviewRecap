from base64 import b64decode

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .parser.scraper import scrape
from .parser.translator import translate


@api_view(["GET"])
def get_product(request, b64):

    url = b64decode(b64).decode("utf-8")
    url_parts = url.split("/")
    name = url_parts[0] + url_parts[2]
    print(url)

    try:
        product = Product.objects.get(pk=name)
    except Product.DoesNotExist:
        print("start search")
        scrape_res = translate(url_parts[0] + url_parts[2], scrape(url_parts[0], url_parts[2]))
        print("finish scrape")
        serializer = ProductSerializer(data=scrape_res)
        if serializer.is_valid():
            print("is valid")
            serializer.save()
            product = Product.objects.get(pk=name)
        else:
            print("not valid")
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
