from django.http import HttpResponse


# Create your views here.
def index(request):
    """The index page"""
    return HttpResponse("Hello, world!")
