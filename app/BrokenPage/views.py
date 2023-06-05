from django.shortcuts import render

def BrokenPage(request):
    return render(request, 'broken_page.html')