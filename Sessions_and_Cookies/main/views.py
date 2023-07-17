from django.shortcuts import render
from django.http import HttpResponse
import random

def get_view_count(request):
    request.session['view_count'] = request.session.get('view_count',0) + 1
    return HttpResponse("Your view count is "+str(request.session['view_count']))

def print_cookies(request):
    if 'code' in request.COOKIES:
        code = request.COOKIES['code']
        return HttpResponse('Your code is '+str(code))
    code = random.randint(100000,200000)
    resp = HttpResponse('Welcome to our web. Your code is '+str(code))
    resp.set_cookie('code', code)
    return resp


