from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Article, Feedback, Writer, Comment
from datetime import datetime
from django.db.models import Count, Avg
from django.db.models.functions import Length

# Create your views here.
class SimpleView(View):
    def get(self, request):
        return HttpResponse("GET response")
    
    def post(self, request):
        return HttpResponse("POST response")
    
class ArticleListView(ListView):
    model = Article
    template_name = 'logic/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # return Article.objects.filter(published_date__lte=datetime.now()).order_by('-published_date')
        return Article.objects.all().order_by('-published_date')
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = "logic/article_detail.html"
    context_object_name = 'article'

class FeedbackListView(ListView):
    model = Feedback
    temlate_name = 'logic/feedback_list.html'
    context_object_name = 'feedbacks'

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'logic/feedback_detail.html'
    context_object_name = 'feedback'

total_articles = Article.objects.aggregate(total = Count('id'))
print(total_articles)

average_comments = Comment.objects.aggregate(average = Avg('id'))
print(average_comments)

total_comments = Comment.objects.aggregate(total_comments = Count('id'))
print(total_comments)

articles_per_author = Writer.objects.annotate(article_count = Count('articles'))
for author in articles_per_author:
    print(f'{author.name} has written {author.article_count} articles.')

articles_with_comment_count = Article.objects.annotate(comment_count = Count('comments'))
for article in articles_with_comment_count:
    print(f'{article.title} has {article.comment_count} comments.')

top_author = Writer.objects.annotate(article_count = Count('articles')).order_by('-article_count').first()
print(f'Top author : {top_author.name} with {top_author.article_count} articles.')

average_content_length = Article.objects.annotate(content_length = Length('content')).aggregate(Avg('content_length'))
print(f"Average article content length: {average_content_length['content_length__avg']} characters.")