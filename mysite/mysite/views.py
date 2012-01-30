from django.shortcuts import render_to_response
from django.template import RequestContext, loader
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    c = RequestContext(request)
    c.update({'current_date': now})
    return render_to_response('current_datetime.html',
                              context_instance=c)

def custom_proc(request):
    "A context processor that provides 'app', 'user', 'ip_address'."
    return {'app': 'My app',
            'user': request.user,
            'ip_address': request.META['REMOTE_ADDR']}

def processors_demo(request):
    t = loader.get_template('processors_demo.html')
    c = RequestContext(request, {'message': 'I am processors demo.'},
                       processors=[custom_proc])
    return t.render(c)
