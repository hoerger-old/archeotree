import datetime
from haystack.indexes import *
from haystack import site
from main.models import Student

class StudentIndex(SearchIndex):
    last_name = CharField(model_attr='last_name', document=True)
    first_name = CharField(model_attr='first_name')
    middle_name = CharField(model_attr='middle_name')
    publish_date = IntegerField(model_attr='publish_date')
    title = CharField(model_attr='title')    
    subtitle = CharField(model_attr='subtitle')    
    isbn = CharField(model_attr='isbn')    
# department
# country
# adviser    

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Student.objects
	#.filter(publish_date__lte=datetime.datetime.now())



site.register(Student, StudentIndex)
