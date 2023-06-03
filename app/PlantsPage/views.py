from django.shortcuts import render
from data.models import Plant

def PlantsPage(request):

    plants = Plant.objects.all()

    context = { 'plants': plants }

    return render(request, 'plants_page.html', context)