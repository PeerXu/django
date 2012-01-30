from django.shortcuts import render_to_response
from django.template import RequestContext

def view_tags(request):
    return render_to_response('tags_demo.html',
                              {'message': 'i am demo.'})

def view_tags_current_time(request):
    return render_to_response('tags_current_time.html', {})

def view_tags_current_time2(request):
    return render_to_response('tags_current_time2.html', {})

def view_tags_current_time3(request):
    return render_to_response('tags_current_time3.html', {})
