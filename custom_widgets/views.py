from django.shortcuts import render
from .forms import SurveyForm

# Create your views here.
def home_view(request):
    form = SurveyForm(request.POST)
    context = {'form' : form}
    return render(request, template_name="custom_widgets/home.html", context=context)