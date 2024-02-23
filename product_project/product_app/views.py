from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404
from rest_framework import status
import logging
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger('mylogger')


class ProductAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            logger.info('Data fetched Successfully')
            return Response(data=serializer.data, status=200)
        except:
            logger.error('This is error log')
            return Response(data={'details':'there is an error fetch data'}, status=400)
        
    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Data Added successfully')
            return Response(data=serializer.data, status=201)
        except Exception as e:
            print(e)
            logger.error('This error Added time log')
            return Response(data=serializer.errors, status=400)

class ProductDetailsAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, requpest, pk=None):
        try:
            products = Product.objects.get(pk=pk)
            serializer = ProductSerializer(products)
            logger.info('Fetch data')
            return Response (data=serializer.data, status=200)
        except:
            logger.error('fetching issue')
            return Response(data={'details':'fetching error'}, status=400)
        
    def put(self, request, pk=None):
        try:
            products = Product.objects.get(pk=pk)
            serializer = ProductSerializer(data=products.data, instance=products)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('Updated the value')
            return Response(data=serializer.data, status=205)
        except Product.DoesNotExist as e:
            logger.error("No matching record found")
            return Response(data={'detail': 'Not Found'}, status=404)
        except:
            logger.error('Error Updations')
            return Response(data=serializer.errors, status=400)
        
    def delete(self, request, pk=None):
        try:
            products = Product.objects.get(pk=pk)
            products.delete()
            logger.info('Delete Data')
            return Response(data=None, status=204)
        except:
            logger.error('Delete process error')
            return Response(data={'details':'Not found'}, status=400)