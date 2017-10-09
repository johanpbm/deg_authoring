'''
Created on 20 set. 2017

@author: jbaldeon
'''
from django.contrib import admin

from api.models import DigitalEducationalGame, DigitalEducationalGameImage

class DigitalEducationalGameImageInLine(admin.TabularInline):
    model = DigitalEducationalGameImage
    extra = 3
    
class DigitalEducationalGameAdmin(admin.ModelAdmin):
    inlines = [DigitalEducationalGameImageInLine, ]