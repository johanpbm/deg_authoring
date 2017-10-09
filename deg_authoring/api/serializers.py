'''
Created on 7 set. 2017

@author: jbaldeon
'''

from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models.fields.related import OneToOneField
from django.db.migrations.operations.base import Operation
from django.contrib.gis.db.backends.base import operations
from django.db.models.base import Model

from api.models import DigitalEducationalGame, DGBLInstructionalDesign,\
    Curriculum, DGBLHeader, EduGameAuthoringRegistry, InstructionalDesignModel,\
    IntendedLearningOutcome, DigitalEducationalGameImage, \
    FeaturedGame, CategoryActivityType, ActivityType, EduGameEdition

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('address', 'phone')
        
class UserSerializer(serializers.ModelSerializer):
    #profile = ProfileSerializer()
    #game_configs = serializers.PrimaryKeyRelatedField(many=True, queryset=GameConfig.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username')
    
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CategoryActivityTypeSerializer(serializers.ModelSerializer):
    registered_by = serializers.CharField(source='owner', read_only=True)
    class Meta:
        model = CategoryActivityType
        fields = ('name', 'description', 'registered_by')
        
class ActivityTypeSerializer(serializers.ModelSerializer):
    registered_by = serializers.CharField(source='owner', read_only=True)
    class Meta:
        model = ActivityType
        fields = ('name', 'description', 'category', 'registered_by')
        
class DigitalEducationalGameSerializer(serializers.ModelSerializer):
    registered_by = serializers.CharField(source='owner', read_only=True)
    class Meta:
        model = DigitalEducationalGame
        fields = ('id', 'name', 'description', 'registered_by', 'activity_type')        

class DigitalEducationalGameImageSerializer(serializers.ModelSerializer):
    #registered_by = serializers.CharField(source='owner', read_only=True)
    class Meta:
        model = DigitalEducationalGameImage
        fields = ('digital_educational_game', 'image')    
        
class FeaturedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedGame
        fields = ('digital_educational_game', 'order', 'title')            

class EduGameEditionSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='owner', read_only=True)

    class Meta:
        model = EduGameEdition
        fields = ('game', 'name', 'description', 'author', 'activity_type')
# class EduGameAuthoringData(object):
#     def __init__(self, host, body, created=None):
#         self.host = host
#         self.body = body
#         self.created = created or datetime.now()
#     
        
class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model= Curriculum 
        fields = ('name','description')

class InstructionalDesignModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructionalDesignModel
        fields = ('name', 'description')        
        
class EduGameAuthoringRegistryDataHeader(object):
    def __init__(self, host, operation):
        self.host, self.operation = host, operation        

class EduGameAuthoringRegistryDataHeaderField(serializers.Field):
    #host = serializers.CharField()
    #operation = serializers.CharField()
    
    def to_representation(self, value):
        return 'header: %s, operation:%s' % (value.host, value.operation)
    
    def to_internal_value(self, data):
        data = data.strip('header: ').rstrip(', ')
        host = data
        #data = data.strip('operation: ').rstrip(', ')
        operation = "CONFIG"
        return EduGameAuthoringRegistryDataHeader(host, operation)

class DGBLHeaderSerializer(serializers.Serializer):
    host = serializers.CharField(max_length=200)
    operation = serializers.CharField(max_length=200)

class IntendedLearningOutcomeSerializer(serializers.ModelSerializer):
    #curriculum = CurriculumSerializer(many=True)
    class Meta:
        model = IntendedLearningOutcome
        fields = ('name', 'description')#, 'curriculum')
        
class DGBLInstructionalDesignSerializer(serializers.ModelSerializer):
    registered_by = serializers.CharField(source='owner', read_only=True)
    instructional_design_model = InstructionalDesignModelSerializer()
    curriculum = CurriculumSerializer()
    #ilos = IntendedLearningOutcomeSerializer(many=True)#, source='ilos')
    #intended_learning_outcomes = IntendedLearningOutcomeSerializer(many=True, source='ilos', read_only=True)
    
    class Meta:
        model= DGBLInstructionalDesign 
        fields = ('name','grade', 'description','period', 'area', 'instructional_design_model', 'curriculum', 'ilos', 'registered_by') # 'intended_learning_outcomes',         
        
#     def create(self, validated_data):
#         idmodel_data = InstructionalDesignModel(
#             name = validated_data['instructional_design_model']['name'],
#             description = validated_data['instructional_design_model']['description'])
#         dgbl_instructional_design = DGBLInstructionalDesign(
#             grade=validated_data['grade'],
#             description=validated_data['description'],
#             instructional_design_model=idmodel_data             
#         )
#         #dgbl_instructional_design.set_owner(validated_data['owner'])
#         dgbl_instructional_design.save()
#         return dgbl_instructional_design
    
    def create(self, validated_data):
        #instructional_design_model
        idmodel_data = validated_data.pop('instructional_design_model')
        #idmodel = InstructionalDesignModel.objects.create(**idmodel_data)
        idmodel, created = InstructionalDesignModel.objects.get_or_create(
            name=idmodel_data['name'],
            defaults={'description': idmodel_data['description']},)
        
        #curriculum
        curriculum_data = validated_data.pop('curriculum')
        #icurriculum = Curriculum.objects.create(**curriculum_data)
        icurriculum, created = Curriculum.objects.get_or_create(
            name=curriculum_data['name'],
            defaults={'description': curriculum_data['description']},)

        ilos_data = validated_data.pop('ilos')
        
        dgbl_instructional_design = DGBLInstructionalDesign.objects.create(
            instructional_design_model=idmodel,
            curriculum = icurriculum, 
            **validated_data)
        
        for ilo in ilos_data:
            ilo, created = IntendedLearningOutcome.objects.get_or_create(
                name=ilo['name'],
                defaults={'description': ilo['description']},)
            dgbl_instructional_design.ilos.add(ilo)
        
        #for idmodel_data in idmodels_data:
            #idmodel_data, created = InstructionalDesignModel.objects.get_or_create(name=idmodel_data['name'])
            #dgbl_instructional_design.instructional_design_model.add(idmodel_data)
        
        return dgbl_instructional_design        

    def update(self, instance, validated_data):
        ilos_data = validated_data.pop('ilos')
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.grade = validated_data['grade']
        instance.period = validated_data['period']
        instance.area = validated_data['area']

        for ilo in ilos_data:
            ilo, created = IntendedLearningOutcome.objects.update_or_create(
                name=ilo['name'],
                defaults={'description': ilo['description']},)
            instance.ilos.add(ilo)
        return instance
    
class EduGameAuthoringRegistrySerializer(serializers.ModelSerializer):#Serializer):
#class EduGameAuthoringDataSerializer(serializers.Serializer):
    header = serializers.SerializerMethodField('get_dgbl_header')
    registered_by = serializers.CharField(source='owner', read_only=True)
    game = DigitalEducationalGameSerializer()
    dgbl_instructional_design = DGBLInstructionalDesignSerializer()
    #atrib = serializers.CharField(write_only=True)
    #foo = serializers.ReadOnlyField()
    
    #host = serializers.SerializerMethodField('get_host_field_data')
    #operation = serializers.SerializerMethodField('get_operation_field_data')
    #url = serializers.CharField(source='area') #, read_only=True)
     
    #created = serializers.DateTimeField(source='description')
    
    #game = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name') 
    #game = DigitalEducationalGameSerializer(many=True)#, read_only=True)
    #curriculum = CurriculumSerializer()
    
    def create(self, validated_data):
        #validated_data.pop('atrib', None)
        digital_educational_game_data = validated_data.pop('game')
        digital_educational_game, created = DigitalEducationalGame.objects.get_or_create(
            name=digital_educational_game_data['name'],
            defaults={'description': digital_educational_game_data['description']},)

        my_dgbl_instructional_design_data = validated_data.pop('dgbl_instructional_design')
        my_dgbl_instructional_design, created = DGBLInstructionalDesign.objects.get_or_create(
            name=my_dgbl_instructional_design_data['name'],
            defaults={'grade':my_dgbl_instructional_design_data['grade'],
                      'description': my_dgbl_instructional_design_data['description']},)
                
        edu_game_authoring_registry = EduGameAuthoringRegistry(
            game=digital_educational_game,
            dgbl_instructional_design=my_dgbl_instructional_design
        )
        edu_game_authoring_registry.set_owner(validated_data['owner'])
        edu_game_authoring_registry.save()
        return edu_game_authoring_registry
    
#         curriculum_data = validated_data.pop('curriculum')
#         icurriculum, created = Curriculum.objects.get_or_create(
#             name=curriculum_data['name'],
#             defaults={'description': curriculum_data['description']},)
#         
#         dgbl_instructional_design = DGBLInstructionalDesign.objects.create(
#             instructional_design_model=idmodel,
#             curriculum = icurriculum, 
#             **validated_data)
        
    def get_dgbl_header(self, obj):
        myHeader = DGBLHeader(host="192.168.1.1", operation="INIT")
        serializer = DGBLHeaderSerializer(myHeader) 
        return serializer.data
    
#     def get_operation_field_data(self, obj):
#         return "CONFIG"
#     
#     def get_host_field_data(self, obj):
#         return "http://127.0.0.1:8000"
        
    class Meta:
        #model = DGBLInstructionalDesign
        model = EduGameAuthoringRegistry
        #fields = ('header', 'id', 'atrib', 'foo', 'host', 'operation','description', 'area', 'url', 'created', 'curriculum', 'game')
        fields = ('id', 'header', 'game', 'dgbl_instructional_design', 'registered_by')
    
#class GameConfigSerializer(serializers.ModelSerializer):
    #created_by = serializers.ReadOnlyField(source='created_by.username')
    #game_name = serializers.SlugRelatedField(
    #    read_only=True,
    #    slug_field='name'
    #)
#     game = DigitalEducationalGameSerializer(many=False)
#     
#     class Meta:
#         model = GameConfig
#         fields = ('created', 'name', 'description', 'subject', 'created_by', 'game')   
#         
#     def create(self, validated_data):
#         games_data = validated_data.pop('game')
#         game_config = GameConfig.objects.create(**validated_data)
#         for game_data in games_data:
#             DigitalEducationalGame.objects.create()