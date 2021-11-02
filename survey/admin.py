from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline): # 테이블 형식으로 보여주기
    model = Choice
    extra = 3 # 지정한 값에 따라 한 번에 보여주는 Choice text의 숫자가 결정

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [# 각 필드 순서 변경하고, 분리해서 보여주기
        ('Question Statement',{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse'] }),# 'classes': ['collapse'] 필드 접기
    ]
    inlines = [ChoiceInline] # Question 및 Choice를 한 화면에서 보기
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 레코드 리스트 컬럼 지정

    list_filter = ['pub_date']  # 필터 사이드바 추가
    search_fields = ['question_text']  # 검색박스 추가

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)