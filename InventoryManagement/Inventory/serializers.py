from rest_framework import serializers

from Inventory.models import Inventory


class ListSerializer(serializers.Serializer):
     name = serializers.CharField(max_length=100, required=False)


     def validate(self, attrs):
        name = attrs.get("name")
        return attrs


class InventorySerializer(serializers.ModelSerializer):
   supplier_name = serializers.CharField(source="supplier.name")

   class Meta:
        model = Inventory
        fields = [
                  "name",
                  "supplier_name",
                  "availability"
                 ]


class ListInventorySerializer(serializers.ModelSerializer):
   supplier_name = serializers.CharField(source="supplier.name")

   class Meta:
        model = Inventory
        fields = [
                     "name",
                     "supplier_name"
                 ]





