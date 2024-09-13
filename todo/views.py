from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def index(request):
    item_list = Todo.objects.order_by('-created_at')
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        'forms' : form,
        'list' : item_list,
        'title' : 'Todo List',
    }

    return render(request, template_name="todo/index.html", context=page)


def remove(request, item_id):
    item = Todo.objects.get(id = item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('todo')
