from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from StoreApi.api.models import Product, Order
from StoreApi.api.serializers import ProductSerializer, OrderSerializer, OrderCountSerializer, OrderPriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderStatsView(APIView):

    def get_queryset(self):
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        return Order.objects.filter(date__range=[date_start, date_end])

    def get(self, request):

        serializer = None
        metric = self.request.query_params.get('metric')
        if metric == "count":
            serializer = OrderCountSerializer(self.get_queryset(), many=True)
        elif metric == "price":
            # TODO: Add logic for showing a sum of all the products in an order
            pass
        return Response(serializer.data)

