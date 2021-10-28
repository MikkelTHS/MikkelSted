from django.shortcuts import render

def hjem(request):
  return render(request, "hjem.html")