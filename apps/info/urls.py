from django.urls import path
from .views import info, news, qas

app_name = 'info-center'

urlpatterns = [
  path('com-info.html', info, name='company_info'),
  path('info/<int:info_id>.html', info, name='info_detail'),
  path('news.html', news, name='news'),
  path('news/news-detail-<int:news_id>.html', news, name='news_detail'),
  path('question-and-answer.html', qas, name='qas'),
  path('question-and-answer-<int:q_id>.html', qas, name='qas_detail'),
]