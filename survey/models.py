import datetime
from django.db import models  # 상속받아 테이블들을 클래스 형태로 만들어줌
from django.utils import timezone


# Create your models here.
# 각 클래스의 변수는 컬럼 명, id는 부모에 정의되어 있어 따로 정의 할 필요 X
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 타입은 문자열이므로 CharField()메서드 사용
    pub_date = models.DateTimeField('date published')  # 타입은 시간나타내는 것이므로 DateTimeField()메서드 사용

    # self.question_text 출력
    def __str__(self):
        return self.question_text

    # 최근에 생성된 질문인지 구분
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # 외래키, 첫번째 인자: 참조되는 모델 클래스 이름,
    # 두번째 인자: 참조하는 테이블의 행이 삭제되면 대응되는 행들도 같이 삭제, 갱신되면 같이 갱신
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # 타입은 문자열이므로 CharField()메서드 사용
    votes = models.IntegerField(default=0)  # 타입은 정수타입이므로 IntegerField()메서드 사용

    # self.choice_text 출력
    def __str__(self):
        return self.choice_text
