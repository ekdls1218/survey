## 앱 수준의 경로 패턴 정의
from django.urls import path
from . import views

app_name='survey'

urlpatterns=[
    #  path 함수는 path(route, view, kwargs, name) 형태로 호출,
    # route(주소), view(route의 주소로 접근했을 때 호출할 view), kwargs(뷰에 전달할 값들), name(route의 이름)

    ### Generic view (class-based view)
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    ##path('', views.index, name='index'), # config.urls에서 1차 처리 후 남은 경로로 전달 된 것이기 때문에 빈 문자열로 보이게 됨
    # <>는 변수 의미, 해당값을 뷰에 인자로 전달 
    ##path('<int:question_id>/', views.detail, name='detail'), # url 마지막이 숫자로 끝나면 views.detail로 이동
    ##path('<int:question_id>/results/', views.results, name='results'), # url 마지막이 results로 끝나면 views.results로 이동
    ##path('<int:question_id>/vote/', views.vote, name='vote'), # url 마지막이 vote로 끝나면 views.vote로 이동
]
