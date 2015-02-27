from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from topics.models import TopicStream
# Create your views here.
def show_all(request):
    return HttpResponse('show all')
