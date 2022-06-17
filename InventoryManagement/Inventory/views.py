from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework.response import Response

from Inventory.serializers import ListSerializer
from Inventory.serializers import InventorySerializer
from Inventory.serializers import ListInventorySerializer
from Inventory.models import Inventory


class InventoryView(GenericAPIView):
    serializer_class = ListSerializer


    def get(self, request):
        request_data = request.query_params
        serializer = self.serializer_class(data=request_data)
        if not serializer.is_valid():
            print(serializer.errors)
            error_parameter = serializer.errors.popitem()[0]
            error_message = serializer.errors.popitem()[1][0]
            error_message = error_message
            data = {
                        "message": error_message,
                        "status": "error",
                        "status_code": status.HTTP_404_NOT_FOUND,
                   }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        
        name = serializer.validated_data.get("name")

        if name:
            inventories = Inventory.objects.filter(Q(name__icontains=name))
        else:
            inventories = Inventory.objects.all()

        serializer = InventorySerializer(inventories, many=True, context={"request": request})
        data = {
                    "message": "Successfully Retrieved",
                    "status": "success",
                    "status_code": status.HTTP_200_OK,
                    "data": serializer.data,
               }
        return Response(data, status=status.HTTP_200_OK)


class InventoryList(generics.ListAPIView):


    def get(self, request, format=None):
        queryset = Inventory.objects.all()
        serializer_class = InventorySerializer(
            instance=queryset, many=True, context={"request": request}
        )
        inventories = Inventory.objects.all()
        serializer = ListInventorySerializer(inventories, many=True, context={"request": request})
        data = {
                    "message": "Successfully Retrieved",
                    "status": "success",
                    "status_code": status.HTTP_200_OK,
                    "data": serializer.data,
               }
        return Response(data, status=status.HTTP_200_OK)


class InventoryDetail(DetailView):
    model = Inventory
    template_name = 'inventory_details.html'
