from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
# Create your views here.

def IndexView(request):
	question_list = Question.objects.order_by('pub_date')
	return render(request, 'polls/index.html', {'question_list': question_list})

	# return HttpResponse('투표할 질문들을 보여주는 Index Page')

def DetailView(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

	# return HttpResponse('{} 질문의 제목, 그리고 선택지들을 보여주는 Detail Page'.format(question_id))

def ResultView(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html', {'question': question})

	# return HttpResponse('{} 해당 질문을 투표한 후, 결과를 보여주는 Result Page'.format(question_id))

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	selected_choice = question.choice_set.get(pk=request.POST['choice'])
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

	# return HttpResponse('{} 지금 투표하기 기능을 실행중입니다'.format(question_id))



	







