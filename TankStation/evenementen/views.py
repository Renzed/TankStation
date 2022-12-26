from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
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
    context = {
        'komende_tanktiviteiten': komende_tanktiviteiten,
    }
    return render(request, 'main.html', context)

def test(request):
    return HttpResponse("yess")

@login_required
def detail(request, tanktiviteit_id):
    tanktiviteit = get_object_or_404(Tanktiviteit, pk=tanktiviteit_id)
    deelnemers = tanktiviteit.inschrijvingen.all()
    context = {
        'ttvt': tanktiviteit,
        'deelnemers': deelnemers,
    }
    return render(request, 'detail.html', context)
    #return HttpResponse(f"Dit is tanktiviteit {tanktiviteit.naam}, met id {tanktiviteit_id}, aangemaakt op {tanktiviteit.aanmaakmoment} en plaatsvindend op {tanktiviteit.wanneer} met inschrijvingen {tanktiviteit.inschrijvingen.first().plaatser}")


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
        inschrijving.save()
        # inschrijving.plaatser = request.user
        return HttpResponseRedirect(reverse('evenementen:Tanktiviteit detail', args=(tanktiviteit_id,)))


def uitschrijven(request, tanktiviteit_id, inschrijving_id):
    # TODO: zorgen dat ie de inschrijving uit het lijstje van account gelinkte inschrijvingen vist
    inschrijving = get_object_or_404(Inschrijving, pk=inschrijving_id)
    inschrijving.delete()
    return HttpResponseRedirect(reverse('evenementen:Tanktiviteit detail', args=(tanktiviteit_id,)))
