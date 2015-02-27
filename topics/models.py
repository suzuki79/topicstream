from django.db import models
from mongiengine import *
# Create your models here.
class TopicStream(Document):

    category_cd = StringField()
    doc_list    = ListField()
