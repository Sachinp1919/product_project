from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
import logging


logger = logging.getLogger('mylogger')

class UserAPI(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            logger.info('User created successfully')
            return Response(data=serializer.data, status=201)
        except:
            logger.error('User created time error')
            return Response(data=serializer.errors, status=404)