from rest_framework.serializers import Serializer
from .models import Shop
from .serializers import ShopSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
import logging

# logger = logging.getLogger('django')

class ShopView(APIView):
    keycloak_roles = {
        'GET': ['judge'],
    }
    def get(self, request, pk=None, format=None):
        id = pk 
        if id is not None:
            # logger.debug("ID Provided")
            # logger.info("ID Provided")
            # logger.warning("ID Provided")
            # logger.error("ID Provided")
            # logger.critical("ID Provided")
            shop = Shop.objects.get(id=id)
            serializer = ShopSerializer(shop)
            return Response(serializer.data)
        else:
            # logger.info("No ID provided")
            # logger.warning("ID Provided")
            shop = Shop.objects.all()
            serializer = ShopSerializer(shop,many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Your data inserted successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,{'error':'somthing went wrong'},status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        id = pk
        shop = Shop.objects.get(id=id)
        serializer = ShopSerializer(shop,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'your complete data updated succesfully'}, status = status.HTTP_206_PARTIAL_CONTENT)

        else:
            return Response(serializer.errors,{'error':'something went wrong'},status = status.HTTP_400_BAD_REQUEST)

    
    def patch(self, request, pk, format=None):
        id = pk
        shop = Shop.objects.get(id=id)
        serializer = ShopSerializer(shop,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'your complete partial updated succesfully'}, status = status.HTTP_206_PARTIAL_CONTENT)

        else:
            return Response(serializer.errors,{'error':'something went wrong'},status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        shop = Shop.objects.get(id=id)
        shop.delete()
        return Response({'success':'record deleted succesfully'}, status = status.HTTP_202_ACCEPTED)
        
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]


        
