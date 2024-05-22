from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from medicine_store.models import med_kit
from medicine_store.forms import ProductForm
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
    
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    return Response({'logged in successfully'},status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes((AllowAny,))
def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response({'product created'}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny,))
def list_products(request):
    products = med_kit.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes((AllowAny,))
def update_product(request, pk):
    product = get_object_or_404(med_kit, pk=pk)
    form = ProductForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((AllowAny,))
def delete_product(request, pk):
    try:
        product = med_kit.objects.get(pk=pk)
    except med_kit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("deleted successfully")

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def searchmed(request):
    medicinename = request.data.get('name')
    
    if medicinename is None:
        return Response("Please provide a valid medicine name", status=status.HTTP_400_BAD_REQUEST)
    
    products = med_kit.objects.filter(Medicinename__icontains=medicinename)
    if products.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response("No medicine available with the provided name", status=status.HTTP_404_NOT_FOUND)