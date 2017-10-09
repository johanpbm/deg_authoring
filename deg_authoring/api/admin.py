# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import Curriculum, IntendedLearningOutcome, InstructionalDesignModel, DigitalEducationalGame, DGBLInstructionalDesign, EduGameAuthoringRegistry

# Register your models here.
admin.site.register(Curriculum)
admin.site.register(IntendedLearningOutcome)
admin.site.register(InstructionalDesignModel)
admin.site.register(DigitalEducationalGame)
admin.site.register(DGBLInstructionalDesign)
admin.site.register(EduGameAuthoringRegistry)


