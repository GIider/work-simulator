from django.http import HttpResponse
from django.template import RequestContext, loader


def page(request, current):
    """View for pages"""
    current = current or 'index'
    template = loader.get_template('pages/{}.html'.format(current))
    context = RequestContext(request, {'current': current})
    return HttpResponse(template.render(context))
