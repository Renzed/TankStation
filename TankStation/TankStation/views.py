from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required
def index(request):
    komende_ins = request.user.inschrijvingen.filter(tanktiviteit__wanneer__gt=timezone.now())
    tr = request.user.rekening
    context = {
        'ins': komende_ins,
        'tr': tr
    }
    return render(request, 'base.html', context)
