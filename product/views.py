

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product  # Import your model
from .serializers import MyDataSerializer  # Import the serializer

class MyDataAPIView(APIView):
    def get(self, request):
        # Retripeve data from your model or any source
        products = Product.objects.all()  # Example: Fetching all objects from YourModel
                
        # Check if there are any instances in the queryset
        if products.exists():
            serializer = MyDataSerializer(products, many=True)
            serialized_data = serializer.data
            # Check the serialized data
            print(serialized_data)
        else:
            print("No data found in the Product model.")
        
        print(serializer.data)
        # Return the serialized data in the response
        return Response(serializer.data)
        