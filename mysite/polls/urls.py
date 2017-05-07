from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
	url(r'^$', views.IndexView, name='index'), #/polls/
	url(r'^(?P<question_id>[0-9]+)/$', views.DetailView, name='detail'), #/polls/1/
	url(r'^(?P<question_id>[0-9]+)/result/$', views.ResultView, name='result'), #/polls/1/result
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote') #/polls/1/vote
]

