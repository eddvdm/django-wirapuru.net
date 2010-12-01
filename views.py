__author__ = 'Eduardo Vaz de Mello'


from django.http import HttpResponse

def woah(request):
    return HttpResponse("<h1>Woah, it works! But only doing the restart.txt thing to refresh..</h1>") 