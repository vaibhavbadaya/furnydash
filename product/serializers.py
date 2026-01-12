# serializers.py

from rest_framework import serializers
from brand.serializers import BrandSerializer
from .models import Product  # Import your model

class MyDataSerializer(serializers.Serializer):
    
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    brand= BrandSerializer()

    class Meta:
        model = Product
        fields = ('name','description','brand')

    def get_name(self, obj):
        return obj.name 
    
    def get_description(self,obj):
        return obj.description
    
    def get_brand(self,obj):
        return obj.brand

