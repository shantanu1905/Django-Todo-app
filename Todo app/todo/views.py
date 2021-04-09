from django.shortcuts import render ,HttpResponse ,redirect 
from todo.models import Taskdata
from django.contrib import messages

# Create your views here.

def taskList(request):
    if request.method == "POST":
        title= request.POST['title']
        desc= request.POST['desc']
        ins=Taskdata(TaskTitle=title , taskdesc=desc)
        ins.save()
        messages.success(request, 'your Task is being added Todo-List')

        
    return render(request,"tasks.html")
        
       
    

def taskfinal(request):
    allTasks = Taskdata.objects.all()
    #for item in allTasks:
      #  print(item.TaskTitle)
    context = {'Tasks':allTasks}

    return render(request,"tasklist.html", context)



def delete(request , Taskdata_id):
    item= Taskdata.objects.get(pk=Taskdata_id)
    item.delete()
    messages.success(request, 'your Task has been deleted successfullly')
    return redirect("tasks")