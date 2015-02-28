
from django.db import models
from mongoengine import *
from bson import ObjectId
import urllib2
from collections import Counter
# Create your models here.

class TopicStream(Document):

    category_cd     = StringField()
    topic_name      = StringField()

    #topic_stream  = [{topic_date:2014/1/3, doc_id_list:[12,21], doc_list:[d1,d2]},
    #                {topic_date:2014/1/3, doc_id_list:[12322,334dsdf], doc_list:[d1,d2]},..]
    topic_stream    = ListField()
    hot_topic_flg   = BooleanField()
    last_added_date = DateTimeField()
    stream_count    = IntField()

    def load_contents(self):
        #for topic in self.topic_stream:
        #    topic["doc_list"] = AnalyzedContentData.objects(id__in = topic["doc_id_list"])

        self.article_count = 0
        for t in self.topic_stream:
            for d in t["doc_id_list"]:
                self.article_count += 1

        self.topic_stream.sort(key = lambda x: x["topic_date"])
        first_day = self.topic_stream[0]["topic_date"]
        self.span = "{0} ~ {1}".format(first_day, self.last_added_date)

        doc_list = AnalyzedContentData.objects(id__in = self.topic_stream[0]["doc_id_list"])
        self.summary = doc_list[0].body[0:200]
        self.image = self.image()

    def sort(self):
        self.topic_stream.sort(key = lambda x: x["topic_date"])

        for topic in self.topic_stream:
            docs = AnalyzedContentData.objects(id__in = topic["doc_id_list"])
            topic["doc_list"] = []
            for d in docs:
                topic["doc_list"].append(d.to_cashed_data())



    def latest(self):

        self.topic_stream.sort(key = lambda x: x["topic_date"])
        #get latest
        return self.topic_stream[-1]

    def image(self):
        for t in self.topic_stream:
            docs = AnalyzedContentData.objects(id__in = t["doc_id_list"])
            for doc in docs:
                url = doc.image
                try:
                    f = urllib2.urlopen(url)
                    # do stuff
                    return url
                except Exception:
                    print "Not Found"

        print "NotFound"
        return ""


class CashedDoc:
    def __init__(self, analyzed_content_data):
        self.original_data = analyzed_content_data
        tfidfs = analyzed_content_data.tfidfs
        tfidfs = Counter(tfidfs)
        self.tfidfs = tfidfs.most_common()[0:20]
        self.category_tfidfs = analyzed_content_data.category_tfidfs
        self.id = analyzed_content_data.id
        self.category = analyzed_content_data.category
        self.title = analyzed_content_data.title
        self.body = analyzed_content_data.body
        self.word_cnt = analyzed_content_data.word_cnt



class AnalyzedContentData(Document):
    objectid = ObjectIdField()
    category = StringField()
    title = StringField()
    body = StringField()
    link = StringField()
    image = StringField()
    image_size = IntField()
    word_cnt = DictField()
    teacher_classifier = ListField()
    #new field below
    learn_category = ListField()
    tfidfs         = DictField()
    created_at    = DateTimeField()
    tsfsidf_list  = ListField()
    category_tfidfs = DictField()

    def to_cashed_data(self):
        return CashedDoc(self)



class Category(Document):
    cd = StringField()
    name = StringField()
