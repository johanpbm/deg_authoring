'''
Created on 18 set. 2017

@author: jbaldeon
'''

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.urls import reverse

from api.models import DigitalEducationalGame, FeaturedGame, EduGameEdition
from deg_authoring.forms import UploadImageForm

def index(request):
    return HttpResponseRedirect("/deg_authoring/")
    
def game_list(request):
    latest_game_list = DigitalEducationalGame.objects.order_by('-name')#[:3]
    #latest_game_list = FeaturedGame.objects.order_by('order')    
#     template = loader.get_template('deg_authoring/index.html')
#     context = {
#         'latest_game_list': latest_game_list,
#     }
#    return HttpResponse(template.render(context, request))
    context = {'latest_game_list': latest_game_list}
    #
    #print ("El primer elemento de la lista es: " + latest_game_list[0].digital_educational_game.name)
    if (latest_game_list.count()>0):
        print ("El primer elemento de la lista es: " + latest_game_list[0].name)
    for element in latest_game_list:
        print(element.images.all())
    #
    return render(request, 'deg_authoring/index.html', context)

def game_detail(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)    

def edition_list(request):
    editions_list = EduGameEdition.objects.order_by('name')
    context = {'editions_list': editions_list}
    return render(request, 'deg_authoring/editions_list.html', context)
    
def edition_detail(request, game_edition_id):
    game_edition = get_object_or_404(EduGameEdition, pk=game_edition_id)
    return render(request, 'deg_authoring/edition_detail.html', {'game_edition': game_edition})    
    
def save_edition(request, game_edition_id):
    game_edition = get_object_or_404(EduGameEdition, pk=game_edition_id)
    try:
        game = game_edition.game
    except (KeyError, DigitalEducationalGame.DoesNotExist):
        return render(request, 'deg_authoring/edition_detail.html', {
            'game_edition': game_edition,
            'error_message': "The game don't exist.",
            })
    else:
        game_edition.game = game
        game_edition.save()
        return HttpResponseRedirect(reverse('edition_results', args=
                                        (game_edition.id,)))        
             
@login_required
def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImageForm()
    
    #return render_to_response('deg_authoring/upload.html', locals(), context_instance=RequestContext(request))
    context_instance=RequestContext(request).flatten()    
    return render(request, 'deg_authoring/upload.html', context_instance)
                               
def home_view(request):
    return render('base.html')                               