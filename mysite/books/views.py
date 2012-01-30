from django.shortcuts import render_to_response
from django.template import RequestContext, loader

def book_info(request):
    return render_to_response('book.html',
                              {'bookid': '123321-123321-123321'})
