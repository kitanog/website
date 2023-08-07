from django.urls import path
from . import views

'''
Add name spaces to the URL conf file in the project, this applies to future projects too, so that Django knows what 
belongs where
'''
app_name = 'polls'

#The section below uses the default built in Django views
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]


'''
#Manually defining the URLS, instead of using the built in default views
urlpatterns = [
	# INDEX - ex: /polls/
	path('', views.index, name='index'),

	# DETAIL - ex: /polls/5
	path('<int:question_id>/', views.detail, name ='detail'),

	# RESULTS - ex: /polls/5/results
	path('<int:question_id>/results/', views.results, name='results'),

	# VOTE - ex: /polls/5/vote
	path('<int:question_id>/vote/',views.vote, name='vote'),
]
'''