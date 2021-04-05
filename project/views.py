from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.template import loader
from django.http import HttpResponse
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
def uploadMass(request):
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
def allImages(request):
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
