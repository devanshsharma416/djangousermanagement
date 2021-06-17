from .models import Todo
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request, 'todo.html', {'todos': todo})


def delete(request,pk):
    todo = Todo.objects.get(id = pk)
    print(todo)
    todo.delete()
    return redirect('/')

def update(request):
    pass