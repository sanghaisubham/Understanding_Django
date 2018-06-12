from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm,NewTodoForm
# Create your views here.
def index(request):
    todo_list=Todo.objects.order_by('id')
    #form=TodoForm()
    newtodoform=NewTodoForm()
    context={'todo_list':todo_list,'form':newtodoform}
    return render(request,'todo/index.html',context)

@require_POST #Takes care that this view only takes POST request
def addTodo(request):
    form=TodoForm(request.POST) 
    newtodoform=NewTodoForm(request.POST)
    print(request.POST['text'])
#     instantiated with the data passed in the form.request.POST takes all the post data we have in in the form
#     if form.is_valid:
#         new_todo=Todo(text=form.cleaned_data['text'])
#         new_todo.save()
    if newtodoform.is_valid():
    	new_todo=newtodoform.save()
        
    return redirect('index') 

def completeTodo(request,todo_id):
    todo=Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()
    return redirect('index')
    
def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete() #Remove that from Database
    return redirect('index')

def deleteall(request):
    Todo.objects.all().delete() #Remove that from Database
    return redirect('index')
    
#refresh to show the changes (redirect to same page)