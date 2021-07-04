from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.template import loader
from django.http import HttpResponse, JsonResponse
from project.models import EmployeeDetails
from project.models import Image

from django.conf import settings

## for testing images
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import EmployeeForm

from django.views.generic import DetailView
from .models import Employee

class EmployeeImage(TemplateView):
    form = EmployeeForm
    template_name = 'emp_image.html'
    def post(self, request, *args, **kwargs):

        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

@csrf_exempt
def uploadEmpMass(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    context = {'title': 'welcome', 'form': form}
    if form.is_valid():
        form.save()
        context = {'form': form, 'title': 'thanks'}
    return render(request, 'emp_image.html', context)

## path('emp-image/<int:pk>/',EmpImageDisplay.as_view(), name = 'display')
class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'

## test see all images
def allEmpImages(request):
    image_list = Employee.objects.all()
    template = loader.get_template('allImages.html')
    context = {"image_list":image_list}
    return HttpResponse(template.render(context,request))

## testing taking in post from jquery
@csrf_exempt
def do_something(request):
    age = 1
    if request.POST:
        name = request.POST.getlist('name')[0]
        age = request.POST.getlist('age')[0]

    # can't get it to redirect right now but it should be fine, maybe redirect in jquery
    return HttpResponseRedirect(reverse_lazy('display', kwargs={'pk': age}))

############### FINAL BUILD STUFF #####################
## for final build
from .models import Image
from .models import Folder
from .models import Task
from .models import User

from .forms import ImageForm, FolderForm, TaskForm, UserForm, LoginForm, MassUsersForm

import random

class ImageUpload(TemplateView):
    form = ImageForm
    template_name = 'emp_image.html'
    def post(self, request, *args, **kwargs):

        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class UserCreate(TemplateView):
    form = UserForm
    template_name = 'emp_image.html'
    def post(self, request, *args, **kwargs):

        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class UserLogin(TemplateView):
    form = LoginForm
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST, request.FILES)

        if form.is_valid():
            #obj = form.save()
            user = form.cleaned_data['name']
            pw = form.cleaned_data['password']
            
            userObjects = (User.objects.filter(name=user))

            if userObjects[0].password == pw:
                request.session['name'] = userObjects[0].name
                # maybe redirect to consent page
                #return HttpResponseRedirect(reverse_lazy('user', kwargs={'pk': userObjects[0].id}))
                return HttpResponseRedirect(reverse_lazy('consent'))
            else:
                print("Your username and password didn't match.")

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class MassUsers(TemplateView):
    form = MassUsersForm
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):

        form = MassUsersForm(request.POST)

        if form.is_valid():
            #obj = form.save()
            numUsers = form.cleaned_data['numberUsers']
            
            for i in range(numUsers):
                if(i<(numUsers/4)):
                    u = User(name = ("u"+str(random.randrange(8000)+9000)), password=("p"+str(random.randrange(100))), sexAssign = "M", order="ascending", tasksDone=0)
                    u.save()
                elif(i<(numUsers/2)):
                    u = User(name = ("u"+str(random.randrange(8000)+9000)), password=("p"+str(random.randrange(100))), sexAssign = "M", order="descending", tasksDone=0)
                    u.save()
                elif(i<(3*numUsers/4)):
                    u = User(name = ("u"+str(random.randrange(8000)+9000)), password=("p"+str(random.randrange(100))), sexAssign = "F", order="ascending", tasksDone=0)
                    u.save()
                else:
                    u = User(name = ("u"+str(random.randrange(8000)+9000)), password=("p"+str(random.randrange(100))), sexAssign = "F", order="descending", tasksDone=0)
                    u.save()


            
            return HttpResponseRedirect(reverse_lazy('allusers'))
            
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
## test see all images
def allUsers(request):
    user_list = User.objects.all()
    template = loader.get_template('allusers.html')
    context = {"user_list":user_list}
    return HttpResponse(template.render(context,request))
#####
### TODO
######
# then after that just kind of need to make a script for mass user generation  I guess on like an obscure url you could do this one
# task selection randomization
# reorder the link progression through the website
# have kill button url? maybe not for now
# have get all tasks button or database searcher maybe
# have database deleter button?

@csrf_exempt
def uploadMass(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    context = {'title': 'welcome', 'form': form}
    if form.is_valid():
        form.save()
        context = {'form': form, 'title': 'thanks'}
    return render(request, 'emp_image.html', context)

@csrf_exempt
def uploadFolder(request):
    form = FolderForm(request.POST or None, request.FILES or None)
    context = {'title': 'welcome', 'form': form}
    if form.is_valid():
        form.save()
        context = {'form': form, 'title': 'thanks'}
    return render(request, 'emp_image.html', context)

## path('emp-image/<int:pk>/',EmpImageDisplay.as_view(), name = 'display')
class ImageDisplay(DetailView):
    model = Image
    template_name = 'image_display.html'
    context_object_name = 'emp'

class TaskDisplay(DetailView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'emp'

class UserDisplay(DetailView):
    model = User
    template_name = 'user_display.html'
    context_object_name = 'emp'

## test see all images
def allImages(request):
    image_list = Image.objects.all()
    template = loader.get_template('allImages.html')
    context = {"image_list":image_list}
    return HttpResponse(template.render(context,request))

## test see all images
def allTasks(request):
    task_list = Task.objects.all()
    template = loader.get_template('alltasks.html')
    context = {"task_list":task_list}
    return HttpResponse(template.render(context,request))

## task
def task(request):
    userObjects = (User.objects.filter(name=request.session['name']))

    #check if user is done with their tasks
    if(userObjects[0].tasksDone>=3):
        print("tasksdone: ",userObjects[0].tasksDone)
        #return HttpResponseRedirect(reverse_lazy('post_process'))
        return HttpResponseRedirect(reverse_lazy('doneTasks'))

    # select a random folder of appropriate sex
    folders = Folder.objects.filter(sex = userObjects[0].sexAssign)
    taskfolder = folders[random.randrange(len(folders))].folder
    print("len of folders:",len(folders),"taskfolder:",taskfolder)

    taskorder = userObjects[0].order
    taskuser = userObjects[0].name
    print(taskuser)
    image_list = Image.objects.filter(folder=taskfolder)
    template = loader.get_template('task.html')
    context = {"image_list":image_list, "taskfolder":taskfolder, "taskorder":taskorder, "taskuser":taskuser, "folderlength":len(image_list)}
    return HttpResponse(template.render(context,request))


## create the task object!
@csrf_exempt
def submit_task(request):
    userObjects = (User.objects.filter(name=request.session['name']))

    idvar = -1
    if request.POST:
        taskfolder = request.POST.getlist('folder')[0]
        taskorder = request.POST.getlist('order')[0]
        taskuser = request.POST.getlist('user')[0]
        taskindex = request.POST.getlist('indexStop')[0]

        b = Task(folder=taskfolder, indexStop=taskindex, user = taskuser, order=taskorder)
        b.save()
        idvar = b.id

        #update the users task count
        
        userObject = userObjects[0]
        userObject.tasksDone = (userObject.tasksDone + 1)
        userObject.save()
        
    
    # can't get it to redirect right now but it should be fine, maybe redirect in jquery
    return JsonResponse({"id":idvar})

## testing taking in post from jquery
@csrf_exempt
def do_something(request):
    age = 1
    if request.POST:
        name = request.POST.getlist('name')[0]
        age = request.POST.getlist('age')[0]

    # can't get it to redirect right now but it should be fine, maybe redirect in jquery
    return HttpResponseRedirect(reverse_lazy('display', kwargs={'pk': age}))

def doneTasks(request):
    return render(request,'doneTasks.html')

## written as test to increment pk
def NextImage(request, pk):
    return HttpResponseRedirect(reverse_lazy('display', kwargs={'pk': pk+1}))

def Showemp(request):
    resultsdisplay=EmployeeDetails.objects.all()
    return render(request,"index.html",{'EmployeeDetails':resultsdisplay})
def index(request):
    return render(request,'index.html')
def instruction(request):
    return render(request,'instruction.html')
def consent(request):
    return render(request,'consent.html')
def process(request):
    return render(request,'process.html')
def post_process(request):
    return render(request,'post_process.html')
def process_page(request):
    
    return render (request, 'process.html')
