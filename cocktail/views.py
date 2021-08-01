from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import CocktailProduct
from .serializers import CocktailProductSerializer, OurUserSerializer


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'ALLCocktails': '/all-cocktails/',
        'AddedCocktail': '/added-cocktail/',
        'RandomDrinks': '/random-cocktail/',
        'Detail view':'/cocktail-detail/<str:pk>/',
        'Latest': '/latest-cocktail/',
        'Create': '/create_cocktail/',
        'Update': '/cocktail-update/<str:pk>/',
        'Delete': '/cocktail-delete/<stk:pk>/',

    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allCocktails(request):
    try:
        cocktails = CocktailProduct.objects.all()
    except CocktailProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CocktailProductSerializer(cocktails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cocktailDetail(request, pk):
    try:
        cocktail_details = CocktailProduct.objects.get(id=pk)

    except CocktailProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CocktailProductSerializer(cocktail_details, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCocktail(request):
    serializer = CocktailProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateCocktail(request, pk):
    try:
        cocktail = CocktailProduct.objects.get(id=pk)
    except CocktailProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if cocktail.user != user:
        return Response({'response': 'You are not authorized'})
    serializer = CocktailProductSerializer(instance=cocktail, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCocktail(request, pk):
    cocktail = CocktailProduct.objects.get(id=pk)
    cocktail.delete()
    return Response("Cocktail deleted successfully")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def randomCocktails(request):
    cocktails = CocktailProduct.objects.all()[:5]
    serializer = CocktailProductSerializer(cocktails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def latestCocktails(request):
    cocktails = CocktailProduct.objects.all().order_by('-datecreated')[:5]
    serializer = CocktailProductSerializer(cocktails, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cocktailCreator(request, pk):
    user =User.objects.get(id=pk)
    cocktails =user.cocktailproduct_set.all()
    serializer = CocktailProductSerializer(cocktails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def endpoinLatest10Cocktails(request):
    cocktails = CocktailProduct.objects.all().order_by('-datecreated')[:10]
    serializer = CocktailProductSerializer(cocktails, many=True)
    return Response(serializer.data)

# The function perform a get request to an API and return 10 latest cocktails
def endpoint(request):
    return render(request,'index.html')

@api_view(['POST'])
def registerUser(request,):
    if request.method =='POST':
        serializer = OurUserSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] ='new user was successfully registered'
            data['email'] =account.email
            data['username'] =account.username
            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors
        return Response(data)
