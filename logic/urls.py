from django.urls import path
from .views import SimpleView, ArticleListView, ArticleDetailView, FeedbackListView, FeedbackDetailView

urlpatterns = [
    # path('', GreetView.as_view(), )
    path('', SimpleView.as_view()),
    path('article_list/', ArticleListView.as_view(), name="article_list"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('feedback_list/', FeedbackListView.as_view(), name="feedback_list"),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name="feedback_detail"),
]