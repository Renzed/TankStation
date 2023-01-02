from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TankRekening

# Create your views here.

@login_required
def index(request):
    tr = get_object_or_404(TankRekening, pk=request.user)
    context = {
        'ver_saldo': tr.geverifieerd_saldo,
        'ver_datum': tr.geverifieerd_op,
        'saldo': tr.saldo(),
        'uit gaan geven': tr.uit_gaan_geven(),
        'evs': tr.inschrijvingen(True),
        'opladingen': tr.opladingen.all()
    }
    return render(request, 'index.html', context)
