from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Tanktiviteit, Inschrijving
from datetime import datetime
from django.utils import timezone


@login_required
def index(request):
    startday = timezone.make_aware(datetime.combine(datetime.now().date(), datetime.min.time()))
    komende_tanktiviteiten = Tanktiviteit.objects.filter(wanneer__gt=startday)
    ingeschreven = [bool(ttvt.inschrijvingen.filter(plaatser=request.user)) for ttvt in komende_tanktiviteiten]
    context = {
        'komende_tanktiviteiten': komende_tanktiviteiten,
        'ingeschreven': ingeschreven,
        'data': zip(komende_tanktiviteiten, ingeschreven)
    }
    return render(request, 'main.html', context)


@login_required
def detail(request, tanktiviteit_id):
    tanktiviteit = get_object_or_404(Tanktiviteit, pk=tanktiviteit_id)
    deelnemers = tanktiviteit.inschrijvingen.all()
    inschrijving = deelnemers.filter(plaatser=request.user)
    if inschrijving:
        inschrijving_id = inschrijving.first().id
    else:
        inschrijving_id = False
    context = {
        'ttvt': tanktiviteit,
        'deelnemers': deelnemers,
        'req': request,
        'nu': timezone.now(),
        'inschrijving_id': inschrijving_id,
    }
    return render(request, 'detail.html', context)
    # return HttpResponse(f"Dit is tanktiviteit {tanktiviteit.naam}, met id {tanktiviteit_id}, aangemaakt op {tanktiviteit.aanmaakmoment} en plaatsvindend op {tanktiviteit.wanneer} met inschrijvingen {tanktiviteit.inschrijvingen.first().plaatser}")


@login_required
def inschrijven(request, tanktiviteit_id):
    tanktiviteit = get_object_or_404(Tanktiviteit, pk=tanktiviteit_id)
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('evenementen:Tanktiviteit detail', args=(tanktiviteit_id,)))
    try:
        opmerking = request.POST['opmerking']
    except KeyError:
        raise Http404("Er ging iets fout, probeer het opnieuw")
    else:
        inschrijving = Inschrijving()
        inschrijving.tanktiviteit = tanktiviteit
        inschrijving.opmerkingen = opmerking
        inschrijving.plaatser = request.user
        inschrijving.save()
        return HttpResponseRedirect(reverse('evenementen:Tanktiviteit detail', args=(tanktiviteit_id,)))


@login_required
def uitschrijven(request, tanktiviteit_id, inschrijving_id):
    # TODO: zorgen dat ie de inschrijving uit het lijstje van account gelinkte inschrijvingen vist
    inschrijving = get_object_or_404(Inschrijving, pk=inschrijving_id)
    if request.user == inschrijving.plaatser:
        inschrijving.delete()
        return HttpResponseRedirect(reverse('evenementen:Tanktiviteit detail', args=(tanktiviteit_id,)))
    else:
        return HttpResponse('Leuk geprobeerd hackermeneer', status=401)


@login_required
def geweest(request, pagesize, page):
    geweeste_ttvt = list(Tanktiviteit.objects.filter(wanneer__lte=timezone.now())[((page-1)*pagesize):((page*pagesize)-1)].values())
    # return HttpResponse(geweeste_ttvt)
    return JsonResponse(geweeste_ttvt, safe=False)
