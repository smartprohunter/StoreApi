from rest_framework import serializers

from StoreApi.api.models import Order, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCountSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(
        source='products.count',
    )

    class Meta:
        model = Order
        fields = ['id', 'date', 'count']


class OrderPriceSerializer(serializers.ModelSerializer):
    # for product in products:
    #     print(product)
    price = serializers.SerializerMethodField()

    def get_price(self):
        products = Order.products.all()
        print(products)
        return products

    class Meta:
        model = Order
        fields = ['id', 'date', 'price']
