from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from topics.models import TopicStream, Category, AnalyzedContentData
# Create your views here.

def show_all(request):
    topics = TopicStream.objects(category_cd = 'WAR')
    categories = Category.objects.all()

    template = loader.get_template('index.html')

    context = RequestContext(request, {'topics':topics, 'categories':categories})

    return HttpResponse(template.render(context))

def get_category_list(request):

    categories = Category.objects.all()

    template = loader.get_template('category.html')
    context = RequestContext(request, {'categories':categories})
    return HttpResponse(template.render(context))

def get_topic_line(request, category_cd):

    topics = TopicStream.objects(category_cd = str(category_cd), stream_count__gte = 2)
    tlist = []
    for t in topics[0:20]:
        t.load_contents()
        tlist.append(t)

    print len(tlist)
    template = loader.get_template('topic_line.html')
    context = RequestContext(request, {'topics':tlist})

    return HttpResponse(template.render(context))

def get_topic_detail(request, topic_id):
    topic = TopicStream.objects.get(id=topic_id)
    #topic.load_contents()
    #for t in topic.topic_stream:
    #    print t
    topic.sort()    

    template = loader.get_template('topic_detail.html')

    context = RequestContext(request, {'topic_stream':topic.topic_stream})
    return HttpResponse(template.render(context))
