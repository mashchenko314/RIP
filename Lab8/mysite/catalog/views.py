from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Bouquet
from .models import Description


def master(request):
    bouquets_list = Bouquet.objects.all()
    context = {'bouquets_list': bouquets_list}
    return render(request, 'catalog/master.html', context)


def detail(request, bouquet_id):
    bouquets_list = Bouquet.objects.all()
    for i in bouquets_list:
        if i.id == bouquet_id:
            bouquet = i
    description = get_object_or_404(Description, pk=bouquet_id)
    return render(request, 'catalog/detail.html', {'bouquet': bouquet, 'description': description})