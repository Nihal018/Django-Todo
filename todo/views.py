from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Task
# Create your views here.



def index(request):    
    todo_list = Task.objects.order_by("date")[:5]
    context = {"todo_list": todo_list}
    return render(request,"todo/index.html",context)

def create_task(request):
    title=request.POST.get("title")
    details=request.POST.get("details")
    task= Task.objects.create(title=title,details=details)
    task.save()
    return redirect(reverse("todo:index"))



def detail(request,pk):
    task= get_object_or_404(Task,pk=pk)
    context={"task" : task}
    return render(request,"todo/detail.html",context)


def delete_task(request,pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    return redirect("todo:index")


