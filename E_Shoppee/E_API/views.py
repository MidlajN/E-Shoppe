from django.shortcuts import render
from .serializer import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from E_App.models import Product, Category
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.

# ---------------- USING SINGLE API VIEW FOR BOTH LISTING AND INDIVIDUAL PRODUCT ------------------
class ProductAPIView(APIView):
    def get(self, request, pk=None, category = None):
        if pk is not None:
            product = get_object_or_404(Product, id=pk)
            serializer = ProductSerializer(product)
        else :
            product = get_list_or_404(Product)
            serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self , request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        product = get_object_or_404(pk=pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)
    
# --------------------- USING SEPERATE API VIEW FOR LISTING AND INDIVIDUAL CATEGORY ---------------------
class CategoryListAPIView(APIView):
    def get(self, request):
        category = get_list_or_404(Category)
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CategoryDetailAPIView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = get_object_or_404(pk=pk)
        category.delete()
        return Response(status=status.HTTP_200_OK)
