from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="question_category")
    question = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.question} - {self.category}"
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answers")
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.question} - {self.answer}"
    
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    stars_earned = models.IntegerField(default=0)  
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.question} - {self.answer}"