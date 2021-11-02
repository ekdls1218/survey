from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect #리다이렉트 기능 사용
from .models import Question, Choice #URL 처리를 위해 reverse 함수 임포트
from django.urls import reverse
from django.template import loader
from django.views import generic

### Generic View (class-based views)
class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'latest_question_list'
    """Return the last five published questions."""
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'survey/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'survey/results.html'



# Create your views here.
##def index(request):
    # latest_question_list 객체를 Question 테이블 객체에서 pub_date 컬럼의 역순으로 정렬하여 5개의 최근 Question 객체를 가져와서 만든다.
    ##latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list]) # ', '.join 는 구분자를 포함한 문자열을 반환
    # return HttpResponse(output)

    ##context ={'latest_question_list': latest_question_list} # 사전형 변수, 템플릿에서 사용할 변수들
    # render()함수 : 템플릿 코드를 로딩한 후 컨텍스트 변수 적용, 그 결과 HttpResponse객체에 담아 반환
    ##return render(request, 'survey/index.html', context) # request, 템플릿 이름, context를 인자로 받음

##def detail(request, question_id):
    # Question테이블에 question_id(투표 항목)가 없으면 404오류 발생
    ##question = get_object_or_404(Question, pk=question_id)
    ##return render(request, 'survey/detail.html',{'question':question})

##def results(request,question_id):
    ##question = get_object_or_404(Question, pk=question_id)
    ##return render(request, 'survey/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: # 키가 ‘choice’에 해당하는 값인 choice.id를 스트링으로 리턴
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist): #검색 조건에 맞는 객체가 없으면 Choice.DoesNotExist 익셉션 발생
        # 사용자에게는 에러 메시지와 함께 질문 항목 폼을 다시 보여줘서 데이터를 재입력하도록 함
        return render(request, 'survey/detail.html', {
            # detail.html 템플릿으로 전달, error_message부분과 연결
            'question':question,
            'error_message': "You didn't select a choice.",
        })
    else: # 정상 처리하는 경우
        selected_choice.votes += 1 # 선택 카운트를 1씩 증가
        selected_choice.save() # 변경 사항을 Choice 테이블에 저장
        # HttpResponseRedirect(url):지정된 url페이지로 redirect할 시 사용됨
        # reverse() 함수는 입력을 받아 URL형식으로 바꿔줌
        return HttpResponseRedirect(reverse('survey:results', args=(question.id,)))

