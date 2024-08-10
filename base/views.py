from django.http import HttpResponse


def home(request):
    return HttpResponse('Fernando, Manon, Fernandinho, Ana e Júlia')
