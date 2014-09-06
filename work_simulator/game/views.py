from django.http import HttpResponse
from django.template import RequestContext, loader


def page(request, parent='', sub=''):
    """View for pages"""
    parent = parent or 'pages'
    sub = sub or 'index'
    template = loader.get_template('{}/{}.html'.format(parent, sub))
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def game(request, sub=''):
    sub = sub or 'index'
    template = loader.get_template('game/{}.html'.format(sub))
    context = RequestContext(request)
    return HttpResponse(template.render(context))
