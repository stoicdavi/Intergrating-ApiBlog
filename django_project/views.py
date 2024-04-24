from jango.shortcuts import render

def index(request):
  return render(request, 'templates/index.html')  