from django.shortcuts import render
import os
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

class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'

## done testing images

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
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path+"/chicago/")
    print(img_list)
    context = {"images": img_list}
    print("context",context)
    # output=Image.objects.all()
    # return render(request,'gallery.html',{"img":img, 'media_url':settings.MEDIA_URL})
    # print("Result",result)
    # return render(request,"process.html",{'Image':output,'media_url':settings.MEDIA_URL})
    return render (request, 'process.html', {'Image ':context})
