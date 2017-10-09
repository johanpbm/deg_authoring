'''
Created on 7 set. 2017

@author: jbaldeon
'''
from django.conf.urls import url, include
#from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^$', views.api_root),
    #url(r'^admin/', admin.site.urls), 
#     url(r'^game_configs/$', views.GameConfigAPIView.as_view(), name='api_game_config'),
#     url(r'^game_configs/(?P<pk>[0-9]+)/$', views.GameConfigItemAPIView.as_view()),
    url(r'^users/$', views.UserListAPIView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailAPIView.as_view()),
    url(r'^edu_games/$', views.DigitalEducationalGameAPIView.as_view(), name='edu-games-list'),
    url(r'^edu_games/(?P<pk>[0-9]+)/$', views.DigitalEducationalGameDetailAPIView.as_view()),
    url(r'^intended_learning_outcomes/$', views.IntendedLearningOutcomeAPIView.as_view(), name='intended-learning-outcome-list'),
    url(r'^intended_learning_outcomes/(?P<pk>[0-9]+)/$', views.IntendedLearningOutcomeDetailAPIView.as_view()),
    url(r'^dgbl_instructional_designs/$', views.DGBLInstructionalDesignAPIView.as_view(), name='dgbl-instructional-designs-list'),
    url(r'^dgbl_instructional_designs/(?P<pk>[0-9]+)/$', views.DGBLInstructionalDesignDetailAPIView.as_view()),                
    url(r'^edu_game_authoring_registry/$', views.EduGameAuthoringRegistryAPIView.as_view(), name='edu-game-authoring-registry'),
    url(r'^edu_games_images/$', views.DigitalEducationalGameImageAPIView.as_view(), name='edu-games-images-list'),
    url(r'^edu_games_images/(?P<pk>[0-9]+)/$', views.DigitalEducationalGameImageDetailAPIView.as_view()),
    url(r'^featured_edu_games/$', views.FeaturedGameAPIView.as_view(), name='featured-edu-games-list'),
    url(r'^featured_edu_games/(?P<pk>[0-9]+)/$', views.FeaturedGameDetailAPIView.as_view()),
    #url(r'^edu_game_authoring/$', views.EduGameAuthoringDataAPIView.as_view(), name='edu-game-authoring'),
#     url(r'^game_configs/digital_edu_games/$', views.DigitalEducationalGameAPIView.as_view(), name='api_digital_edu_game'),
#     url(r'^game_configs/digital_edu_games/(?P<pk>[0-9]+)/$', views.DigitalEducationalGameItemAPIView.as_view()),
    url(r'^category_activity_types/$', views.CategoryActivityTypeAPIView.as_view(), name='category-activity-types-list'),
    url(r'^category_activity_types/(?P<pk>[0-9]+)/$', views.CategoryActivityTypeDetailAPIView.as_view()),
    url(r'^activity_types/$', views.ActivityTypeAPIView.as_view(), name='activity-types-list'),
    url(r'^activity_types/(?P<pk>[0-9]+)/$', views.ActivityTypeDetailAPIView.as_view()),
    url(r'^edu_games_editions/$', views.EduGameEditionAPIView.as_view(), name='edu-games-editions-list'),
    url(r'^edu_games_editions/(?P<pk>[0-9]+)/$', views.EduGameEditionDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]