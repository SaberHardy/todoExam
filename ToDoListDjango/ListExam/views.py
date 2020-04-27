from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest,HttpResponse
from django.contrib import messages
from .models import ToDo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from .forms import ListForm
from django.views.generic import UpdateView


# Create your views here.


@login_required
def list_todo_items(request):
    context={
        'todo_list' : ToDo.objects.all()
        }

    return render(request,'todos/todo_list.html',context)

@login_required
def insert_into_list(request:HttpRequest):
    
    #object from ToDo model
    if request.method == "POST":
        testnull = request.POST['content']
        if testnull == "":
            messages.warning(request,"Add something to do!")
            # messages.info(request,"You need to specify a somthing to do!")
            return redirect("/")

        todo = ToDo(content = request.POST['content'])
        todo.save()
    return redirect('/')

#function for delete the item added
@login_required
def delete_item(request,todo_id):
    todo_to_delete = ToDo.objects.get(id=todo_id)
    todo_to_delete.delete()
    messages.warning(request,"The item successfully deleted!")
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo_list/')
    else:
        form = UserCreationForm()
    return render(request,'account/signup.html',{
        'form':form
        })

@login_required
def edit(request,id):
    
    obj = get_object_or_404(ToDo,id=id)
    form = ListForm(request.POST or None,instance = obj)
    context = {
        "form":form,
        }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request,"You successfully updated the post")
        context= {'form': form}
        return redirect('/')
        # return render(request, 'todos/todo_list.html', context)
        # return redirect('/todo_list')
    else:
         context= {
             'form': form,
             'error': 'The form was not updated successfully. Please enter in a title and content'
         }
    return render(request,'todos/edit.html',context)



# def edit(request,id):
#     item = ToDo.objects.get(id=id)
#     return render(request,'todos/edit.html',{'item':item})



# class UpdateListView(UpdateView):
#     model = ToDo
#     tamplate_name = 'edit.html'
#     fileds = ['content']


# def login(request):
#     return render(request,'account/login.html',{})

# def logout(request):
#     return render(request,'account/logout.html',{})
    