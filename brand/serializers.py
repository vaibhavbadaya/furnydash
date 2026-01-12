# serializers.py

from rest_framework import serializers
from .models import Brand  # Import your model

class BrandSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    contact = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ('name','contact','email')

    def get_name(self, obj):
        return obj.name

    def get_contact(self, obj):
        return obj.contact
    
    def get_email(self, obj):
        return obj.email
