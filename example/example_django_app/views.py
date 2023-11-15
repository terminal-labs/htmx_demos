from django.http import HttpResponse
from django.template.loader import render_to_string

def process(request):
    for key, value in request.GET.items():
        print(f'Key: {key}')
        print(f'Value: {value}')
		
    html = f'''
    process a submit
    '''
    response = HttpResponse(html)
    return response

def fragment(request):
    rendered = render_to_string('frag.html', {'foo': 'bar'})
    response = HttpResponse(rendered)
    return response

def index(request):
    rendered = render_to_string('template.html', {'foo': 'bar'})
    response = HttpResponse(rendered)
    return response
