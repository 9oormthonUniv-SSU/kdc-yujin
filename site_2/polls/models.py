from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published') # ‘date published’ : 관리자 페이지에서 보여질 항목명

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    was_published_recently.boolean = True # 아이콘
    was_published_recently.admin_order_field = 'pub_date' # 정렬 기준
    was_published_recently.short_description = 'Published recently?' # 열 이름


class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0) 

    def __str__(self):
        return self.choice_text
