from django.shortcuts import render, redirect , get_object_or_404
from .models import TodoItem

def todo_list(request):
    todo = TodoItem.objects.all()
    return render(request,'todo_list.html',{'todo':todo})

def create_Todo(request):
    if request.method=='POST':
        title = request.POST['title']
        body = request.POST['body']
        date = request.POST['date']
        time = request.POST['time']
        TodoItem.objects.create(title=title , body=body , date=date , time=time)
        return redirect('todo_list')
    return render(request,'create_todo.html')

def completed(request,todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.complete=True
    todo.save()
    return redirect('todo_list')


def edit_todo(request,todo_id):
    todo = get_object_or_404(TodoItem , id=todo_id)

    if request.method=='POST':
        title = request.POST['title']
        body = request.POST['body']
        date = request.POST['date']
        time = request.POST['time']
        todo.title = title
        todo.body = body
        todo.date = date
        todo.time = time
        todo.save()
        return redirect('todo_list')
    return render(request ,'edit_todo.html',{'todo':todo})

def delete_todo(request,todo_id):
    todo = get_object_or_404(TodoItem , id=todo_id)
    if request.method=='DELETE':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'delete_todo.html')