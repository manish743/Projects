from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Question, Answer, Result
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, template_name="quiz/home.html")

@login_required
def category_list(request):
    categories = Category.objects.all()

    category_data = []
    time_per_question = 10  
    reward_per_question = 10 

    for category in categories:
        questions = Question.objects.filter(category=category)
        total_questions = questions.count()

        # total time and reward for the current category
        total_time = total_questions * time_per_question
        total_reward = total_questions * reward_per_question

        category_data.append({
            'category': category,
            'total_questions': total_questions,
            'total_time': total_time,
            'total_reward': total_reward,
        })

    # total stars earned by the user
    if request.user.is_authenticated:
        total_stars = Result.objects.filter(user=request.user).aggregate(total_stars=Sum('stars_earned'))['total_stars'] or 0

    return render(request, template_name="quiz/quiz_category.html", context={
        'categories' : categories,
        'category_data' :category_data,
        'username': request.user.username,
        'total_stars': total_stars,
    })

@login_required
def question_list(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        questions = Question.objects.filter(category=category)

        correct_answers = 0
        total_questions = questions.count()

        start_time_str = request.session.get('quiz_start_time')
        if start_time_str:
            start_time = datetime.fromisoformat(start_time_str)  
        else:
            start_time = timezone.now()  

        end_time = timezone.now()
        time_spent = round((end_time - start_time).total_seconds())  # time spent in seconds

        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = get_object_or_404(Answer, id=selected_answer_id)
                
                if selected_answer.is_correct:
                    correct_answers += 1
                    stars_earned = 10  
                else:
                    stars_earned = 0

                # saving result for the current user
                Result.objects.create(
                    user=request.user,
                    question=question,
                    answer=selected_answer,
                    is_correct=selected_answer.is_correct,
                    stars_earned = stars_earned,
                )

        # Calculating the user's score
        score = (correct_answers / total_questions) * 100

        # Change starts
        # Calculating bonus stars for perfect score
        # if correct_answers == total_questions:
        #     stars = "⭐" * (correct_answers + 1)
        #     points = 10 * (correct_answers + 1)
        # else:
        #     stars = "⭐" * correct_answers
        #     points = 10 * correct_answers
        # Change ends
        stars = "⭐" * correct_answers
        points = 10 * correct_answers

        # Render the result page with  user's score
        return render(request, 'quiz/result.html', {
            'category': category,
            'score': score,
            'correct_answers': correct_answers,
            'total_questions': total_questions,
            'time_spent' : time_spent,
            'stars' : stars,
            'points' : points
        })

    # handling GET request to show questions
    category_id = request.GET.get('category_id')
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        questions = Question.objects.filter(category=category)
        total_questions = questions.count()

        time_per_question = 10  
        total_time = total_questions * time_per_question

        # Store the quiz start time in the session
        request.session['quiz_start_time'] = timezone.now().isoformat()

        option_labels = ['a', 'b', 'c', 'd']
        return render(request, 'quiz/question_list.html', context={
            'category': category,
            'questions': questions,
            'option_labels' : option_labels,
            'total_time' : total_time,
            # 'time_limit': time_limit,
            # 'start_time': start_time
        })

    return redirect('categories')


@login_required
def answer_list(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    answers = Answer.objects.filter(question = question)
    return render(request, template_name="quiz/answer_list.html", context={
        'question' : question,
        'answers' : answers
    })

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, template_name="authentication/register.html", context={'form' : form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name="authentication/login.html")
    return render(request, template_name="authentication/login.html")

def user_logout(request):
    logout(request)
    return redirect('login')