from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import *
from .serializers import ProductSerializer


@api_view(('GET', ))
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(('GET', ))
def get_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(('POST', ))
def post_product(request):
    data = request.data
    product_type = ProductType.objects.get(id=data['type'])
    data['type'] = product_type
    try:
        Product.objects.get(product_name=data['product_name'],
                            model=data['model'],
                            year=data['year'])
        return Response('El Producto ingresado ya existe. Modifique.')
    except Product.DoesNotExist:
        product = Product.objects.create(
            product_name=data['product_name'],
            model=data['model'],
            year=data['year'],
            price=data['price'],
            type=data['type'],
        )
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


@api_view(('PUT', ))
def put_product(request, pk):
    data = request.data
    products = Product.objects.filter(product_name=data['product_name'],
                                      model=data['model'],
                                      year=data['year'])
    if len(products) <= 1 and products[0].id == pk:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response('El Producto ingresado ya existe. Modifique.')


@api_view(('DELETE', ))
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Producto Eliminado')