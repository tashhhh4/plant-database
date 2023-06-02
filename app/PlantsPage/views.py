from django.shortcuts import render

def PlantsPage(request):
    return render(request, 'plants_page.html')