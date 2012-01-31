from django.shortcuts import render_to_response
from django.template import RequestContext

def view_tags_filter(request):
    return render_to_response('tags_filter.html',
                              {'message': 'i am demo.'})

def view_tags_current_time(request):
    return render_to_response('tags_current_time.html')

def view_tags_current_time2(request):
    return render_to_response('tags_current_time2.html')

def view_tags_current_time3(request):
    return render_to_response('tags_current_time3.html')

def view_tags_my_comment(request):
    return render_to_response('tags_my_comment.html')

def view_tags_my_upper(request):
    return render_to_response('tags_my_upper.html')

def view_demos_test_template(request):
    return render_to_response('test.html')
