# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import urlparse
import os.path
import string

# Create your views here.

def index(request):
    f = open('/Users/nicolas/Desktop/Django-Movies/movies/movies.txt', 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "movieapp/index.html", context)


  #  /Users/nicolas/Desktop/Django-Movies/movies/movies.txt