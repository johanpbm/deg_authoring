# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User

from django.http import HttpResponse

from api.models import DigitalEducationalGame, DGBLInstructionalDesign, EduGameAuthoringRegistry, \
                        IntendedLearningOutcome, DigitalEducationalGameImage, FeaturedGame,\
    CategoryActivityType, ActivityType, EduGameEdition
from api.serializers import DigitalEducationalGameSerializer, EduGameAuthoringRegistrySerializer, \
                    CreateUserSerializer, DGBLInstructionalDesignSerializer, \
                    IntendedLearningOutcomeSerializer, DigitalEducationalGameImageSerializer ,\
    FeaturedGameSerializer, CategoryActivityTypeSerializer, ActivityTypeSerializer,\
    EduGameEditionSerializer
from api.permissions import IsOwnerOrReadOnly

# Create your views here.
    
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         #'game_configs': reverse('api_game_config', request=request, format=format)
#         #'edu_game_authoring_data': reverse('edu-game-authoring', request=request, format=format)
#     })
 
class UserListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer#UserSerializer
    permission_classes = (IsAdminUser,)
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
     
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)        
     
class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer#UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)      

class IntendedLearningOutcomeAPIView(ListCreateAPIView):
    queryset = IntendedLearningOutcome.objects.all()
    serializer_class = IntendedLearningOutcomeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)#, IsOwnerOrReadOnly,)
    
    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)

class IntendedLearningOutcomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = IntendedLearningOutcome.objects.all()
    serializer_class = IntendedLearningOutcomeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
            
class DGBLInstructionalDesignAPIView(ListCreateAPIView):
    queryset = DGBLInstructionalDesign.objects.all()
    serializer_class = DGBLInstructionalDesignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
     
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class DGBLInstructionalDesignDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DGBLInstructionalDesign.objects.all()
    serializer_class = DGBLInstructionalDesignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # IsOwnerOrReadOnly,)

class CategoryActivityTypeAPIView(ListCreateAPIView):
    queryset = CategoryActivityType.objects.all()
    serializer_class = CategoryActivityTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class CategoryActivityTypeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryActivityType.objects.all()
    serializer_class = CategoryActivityTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # IsOwnerOrReadOnly,)

class ActivityTypeAPIView(ListCreateAPIView):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ActivityTypeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # IsOwnerOrReadOnly,)
        

class DigitalEducationalGameAPIView(ListCreateAPIView):
    queryset = DigitalEducationalGame.objects.all()
    serializer_class = DigitalEducationalGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DigitalEducationalGameDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DigitalEducationalGame.objects.all()
    serializer_class = DigitalEducationalGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class DigitalEducationalGameImageAPIView(ListCreateAPIView):
    queryset = DigitalEducationalGameImage.objects.all()
    serializer_class = DigitalEducationalGameImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)#owner=self.request.user)

class DigitalEducationalGameImageDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DigitalEducationalGameImage.objects.all()
    serializer_class = DigitalEducationalGameImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
              
class FeaturedGameAPIView(ListCreateAPIView):
    queryset = FeaturedGame.objects.all()
    serializer_class = FeaturedGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)#owner=self.request.user)

class FeaturedGameDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FeaturedGame.objects.all()
    serializer_class = FeaturedGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)#owner=self.request.user)
    
class EduGameEditionAPIView(ListCreateAPIView):    
    queryset = EduGameEdition.objects.all()
    serializer_class = EduGameEditionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)#owner=self.request.user)

class EduGameEditionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EduGameEdition.objects.all()
    serializer_class = EduGameEditionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)#owner=self.request.user)
                      
class EduGameAuthoringRegistryAPIView(ListCreateAPIView):#APIView):
    #queryset = DigitalEducationalGame.objects.all()
    queryset = EduGameAuthoringRegistry.objects.all()
    #serializer_class = DigitalEducationalGameSerializer
    serializer_class = EduGameAuthoringRegistrySerializer      
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
            
    #def get_serializer(self):
    #    return self.serializer_class
    
#     def get(self, request):
#         instance = EduGameAuthoringDataSerializer()
#         serializer = self.serializer_class(instance)
#         return Response(serializer.data)
#     
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

class MyOwnView(APIView):
    def get(self, request):
        return Response({'some': 'data'})
     
# class DigitalEducationalGameAPIView(ListCreateAPIView):
#     queryset = DigitalEducationalGame.objects.all()
#     serializer_class = DigitalEducationalGameSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  
#     
#     #def perform_create(self, serializer):
#     #    serializer.save(owner=self.request.user)  
#     
# class DigitalEducationalGameItemAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = DigitalEducationalGameSerializer
#     queryset = DigitalEducationalGame.objects.all()    
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)   
#         
# class GameConfigAPIView(ListCreateAPIView):
#     queryset = GameConfig.objects.all()
#     serializer_class = GameConfigSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     
# class GameConfigItemAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = GameConfigSerializer
#     queryset = GameConfig.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)