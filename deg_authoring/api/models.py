# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curriculum (models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    
    def __unicode__(self):
        return u'%s' % self.name
    
class IntendedLearningOutcome (models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    #curriculum = models.ManyToManyField(Curriculum)
    #owner = models.ForeignKey('auth.User', null=True, blank=True)  
    
    def __unicode__(self):
        return u'%s' % self.name
    
    def __getitem__(self, item):
        return getattr(self, item)

class InstructionalDesignModel(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    #curriculum = models.ForeignKey(Curriculum, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name    

class CategoryActivityType(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    owner = models.ForeignKey('auth.User', null=True, blank=True)    

    def __unicode__(self):
        return u'%s' % self.name

class ActivityType(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    category = models.ForeignKey(CategoryActivityType, related_name='activity_types')
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    selected = models.BooleanField(default=False)
        
    def __unicode__(self):
        return u'%s' % self.name
    
    @property
    def is_selected(self):        
        return self.selected         

class DigitalEducationalGame(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    #game_image = models.ImageField(upload_to="images/")
    owner = models.ForeignKey('auth.User', related_name='registered_by', null=True, blank=True)
    activity_type = models.ManyToManyField(ActivityType)   
    #registered_by = models.ForeignKey(User, related_name='registered_by', null=True, blank=True, on_delete=models.CASCADE)
    #@property
    #def get_name(self):
    #    return self.name     
    def __unicode__(self):
        return u'%s' % self.name

class DigitalEducationalGameImage(models.Model):
    digital_educational_game = models.ForeignKey(DigitalEducationalGame, related_name='images')
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    image = models.ImageField(upload_to='deg_authoring/images/games/')
    
    def __unicode__(self):
        return str("Imagen: " + self.image.url)
    
class FeaturedGame(models.Model):
    digital_educational_game = models.ForeignKey(DigitalEducationalGame)
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    order = models.IntegerField()
    title = models.CharField(max_length=30, blank=True, default='')    
    
    def __unicode__(self):
        return str("Juego destacado " + self.order + ": " + self.digital_educational_game.name)

class DGBLHeader(object):
    def __init__(self, host, operation):
        self.host, self.operation = host, operation
                     
class DGBLInstructionalDesign(models.Model):
    name = models.CharField(max_length=100, blank=True, default='' )
    grade = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='') 
    period = models.CharField(max_length=100, blank=True, default='')
    area = models.CharField(max_length=100, blank=True, default='')
    #No considerar IDM, curriculum, Contenido educativo en vez de Instructional Design
    instructional_design_model = models.ForeignKey(InstructionalDesignModel, null=True, blank=True, on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, null=True, blank=True, on_delete=models.CASCADE)
    ilos = models.ManyToManyField(IntendedLearningOutcome)
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    #game = models.ManyToManyField(DigitalEducationalGame)

    def __unicode__(self):
        return u'%s' % self.area + " - " + self.grade + " - " + self.period
    
    def foo(self):
        return 'stuff'
    
    #def header(self):
    #    return DGBLHeader("192.168.200.1", "CONFIG")

class EduGameAuthoringRegistry(models.Model):
    game = models.OneToOneField(DigitalEducationalGame, null=True, blank=True)
    dgbl_instructional_design = models.ForeignKey(DGBLInstructionalDesign, related_name='edu_game_registries_inst_design')
    owner = models.ForeignKey('auth.User', related_name='recorded_by', null=True, blank=True)
    #registered_by = models.ForeignKey(User, related_name='edu_game_registries', null=True, blank=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.game.name, self.dgbl_instructional_design.grade)
    
    def set_owner(self, owner):
        self.owner = owner
        
class EduGameEdition(models.Model):
    game = models.ForeignKey(DigitalEducationalGame, related_name='edu_game_editions')
    name = models.CharField(max_length=100, blank=True, default='' )
    description = models.CharField(max_length=1000, blank=True, default='' )
    owner = models.ForeignKey(User, related_name='edited_by')
    activity_type = models.ManyToManyField(ActivityType)
    
    def __unicode__(self):
        return u'%s - %s' % (self.game.name, self.name)
    
    def contains_activity(self, activity_id):
        for activity in self.activity_type.all:
            if activity_id == activity.id:
                return True
        return False
    
# class Subject(models.Model):
#     name =  models.CharField(max_length=100, blank=True, default='')
#     description = models.CharField(max_length=1000, blank=True, default='')
    

# class DGBLAuthoringDataBody(models.Model):
#     dgbl_instructional_design = models.ForeignKey(DGBLInstructionalDesign, related_name='dgbl_instructional_design', on_delete=models.CASCADE)
#     dgbl_game = models.ForeignKey(DigitalEducationalGame, related_name='dgbl_game', on_delete=models.CASCADE)
# 
# class DGBLAuthoringDataHeader(models.Model):
#     host = models.CharField(max_length=1000, blank=True, default='')
#     operation = models.CharField(max_length=100, blank=True, default='')
#     
# class DGBLAuthoringData(models.Model):
#     header = models.ForeignKey(DGBLAuthoringDataHeader, related_name='header', on_delete=models.CASCADE)
#     body = models.ForeignKey(DGBLAuthoringDataBody, related_name='body', on_delete=models.CASCADE)
        
# class GameConfig(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=100, blank=True, default='')
#     description = models.CharField(max_length=1000, blank=True, default='')
#     subject =  models.CharField(max_length=100, blank=True, default='')
#     created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
#     game = models.ForeignKey(DigitalEducationalGame, related_name='game', on_delete=models.CASCADE)  
#     
#     class Meta:
#         ordering = ('created',)
        
