from django.urls import path
from .views import ArticleView,SingleArticleView




urlpatterns = [
    path("",ArticleView.as_view()),
    path("single/<int:pk>",SingleArticleView.as_view())
]