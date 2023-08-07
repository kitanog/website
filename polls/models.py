import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

'''
NOTE: when this model is applied, it creates database tables with the specified
classes as the table names and the objects as the columns in the table.
Another way to think of this is through System Design.

This is where your class definitions will live
This is not necessary for your site to operate, but it can help
with dynamically generating your site, if your data is defined here.
And stored in a DB, in this case, this is SQLite

This is Also the origin of the APIs you can use to interact with the system
'''
#Create two models Question and Choice

#Question is a question and a publication date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #adding the question text to return, instead of the id?- IMPORTANT TO ADD
    #Defining functions does not add to the columns in the DB?
    def __str__(self):
        return self.question_text
    #adding data for whether or not the question was published in the last day
    #This is just to add some functionality to the Questions API when called
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Choice has two fields - text of the choice and vote tally
#Notice that Choice class references the question
class Choice(models.Model):
    #This links the Question table to this Choice table, relating both ids
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #adding a string to the choice ID
    def __str__(self):
        return self.choice_text