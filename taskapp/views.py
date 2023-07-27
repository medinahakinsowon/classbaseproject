from django.shortcuts import render , redirect
from django.urls import reverse
from . models import Task
from . form import TaskCreateForm
from django.views import View

# Create your views here.

class HomePageView(View):
    template_name = 'index.html'
    def get(self, request):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'taskapp/index.html', context)

class TaskCreateView(View):
    template_name = 'add.html'
    form_class = TaskCreateForm
    initial = {'key': 'value'}

    def get(self, request):
        return render(request, 'taskapp/add.html', 
                      {'form': self.form_class(initial=self.initial)})
    
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('homepage'))
        
        return render(request, 'taskapp/add.html', 
                      {'form': self.form_class(initial=self.initial)})

class TaskDetailView(View):
        template_name = 'detail.html'
        def get(self,request, id):
             task = Task.objects.get(id=id)
             context = {
                  'task':task
             }
             return render(request, 'taskapp/detail.html',context)
        
class TaskUpdateView(View):
     template_name = 'update.html'
     form_class = TaskCreateForm


     def get(self, request, id):
         task = Task.objects.get(id=id)
         form = self.form_class(instance=task)

         context = {
              'form': form
         }

         return render(request, 'taskapp/update.html',context)
     
     def post(self, request, id):
          task = Task.objects.get(id=id)
          form = self.form_class(instance=task,data=request.POST)

          if form.is_valid():
               form.save()
               return redirect(reverse('homepage'))
          
          context = {
               'form': form
          }
          
          return render(request, 'taskapp/update.html',context)

class TaskDeleteView(View):
     def get(self,request, id):
          task = Task.objects.get(id=id)
          task.delete() 

          return redirect(reverse('homepage'))
     

class SettingsViews(View):
     template_name = 'settings.html'
     def get(self, request):

      return render(request, 'taskapp/settings.html')    