from django.urls import path
from news.views import scrape, news_list,breakinghome
from django.urls import path
from . import views
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('news/', news_list, name="home"),
  path('', breakinghome, name="breakinghome"),
  path('about/', views.about, name='about'),  # URL for the about page
]
