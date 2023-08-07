#from django.http import Http404 #not needed cos of the shortcut for get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

#from django.template import loader # not needed since render is being used
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic #importing the generic views

from .models import Choice, Question #This imports data from your Choice and  Questions class in models (i.e your db)

# Create your views here.
#you create views by defining python functions (methods)
#These functions pull data from the database (models) that you defined, you can think of the models
#as the schema for the database?


class IndexView(generic.ListView):
    template_name = 'polls/index.html' #OVERRIDE DEFAULT
    context_object_name = 'latest_question_list' #OVERRIDE DEFAULT 

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html' #OVERRIDE DEFAULT


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Select a choice smarty.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

'''
#These are the old, manually constructed views, you can use the default views provided by Django
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]#first 5 questions
	#template = loader.get_template('polls/index.html') - not needed with render shortcut
	#This is the context dictionary below, with a single key value pair
	context = {
		'latest_question_list': latest_question_list,
		}
	#return HttpResponse(template.render(context, request)) #use render instead
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")

	question = get_object_or_404(Question, pk=question_id) #shortcut for doing the above
	#context is the key value pair of data?
	context = {
		'question':question
		}
	return render(request, 'polls/detail.html', context)
	#return HttpResponse("You're looking at a question %s." % question_id) #making it dynamic with render, 
	# do not need this


def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Select a choice smarty",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

'''
