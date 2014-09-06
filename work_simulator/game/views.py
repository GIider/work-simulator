from django.http import HttpResponse
from django.template import RequestContext, loader


def page(request, parent='', sub=''):
    """View for pages"""
    parent, sub = parent or 'pages', sub or 'index'
    template = loader.get_template('{}/{}.html'.format(parent, sub))
    context = RequestContext(request)
    return HttpResponse(template.render(context))
