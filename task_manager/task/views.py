from django.shortcuts import render,HttpResponse
from .models import Task
from .forms import TaskForm
from django.views import View
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.
def search(request):
    query=request.POST.get('search','')
    if query:
        queryset=(Q(title__icontains=query)) | (Q(property__icontains=query))
        results= Task.objects.filter(queryset).distinct()
    else:
        results=[]
    context ={
        'results':results
    }
    return render(request, 'task/search.html',context)

# def filter(request):
#     print("filter")
#     if request.method=="POST":
#         created_at=request.POST['created_at']
#         due_date=request.POST['due_date']
#         priority=request.POST['priority']
#         completed=request.POST['completed']

#         # queryset=(Q(created_at__icontains=created_at)) & (Q(due_date__icontains=due_date))   # Initialize an empty query
#         # if created_at:
#         #     queryset &= Q(created_at__icontains=created_at)
#         # if due_date:
#         #     queryset &= Q(due_date__icontains=due_date)

        
#         queryset=(Q(created_at__icontains=created_at)) & (Q(due_date__icontains=due_date))
#         results= Task.objects.filter(queryset).distinct()
#         if created_at:
#             results=results.filter(created_at_gte=created_at)
#         if due_date:
#             results=results.filter(due_date_gte=due_date)
#         if completed:
#             results = results.filter(completed=True)
#         if priority:
#             results = results.filter(priority__gte=priority)

#         else:
#             results=[]
        
#         context ={
#         'results':results
#         }
#         return render(request, 'task/search.html',context)

def filter(request):
    if request.method == "POST":
        created_at = request.POST.get('created_at', 'created_at')  # Use get to handle missing keys
        due_date = request.POST.get('due_date', 'due_date')  # Use get to handle missing keys
        priority = request.POST.get('priority', 'priority')  # Use get to handle missing keys
        completed = request.POST.get('completed', False)  # Use get to handle missing keys

        queryset=(Q(created_at__icontains=created_at)) & (Q(due_date__icontains=due_date))   # Initialize an empty query
        if created_at:
            queryset &= Q(created_at__icontains=created_at)
        if due_date:
            queryset &= Q(due_date__icontains=due_date)

        results = Task.objects.filter(queryset).distinct()
        
        if completed:
            results = results.filter(completed=True)
        if priority:
            results = results.filter(priority__gte=priority)  # Assuming priority is a field in your Task model

        else:
            results = []

        context = {
            'results': results
        }
        return render(request, 'task/search.html', context)



class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/taskcreate.html'
    success_url = reverse_lazy('tasklist')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskListView(ListView):
    template_name = 'task/tasklist.html'
    model = Task
    queryset=Task.objects.all()
    context_object_name = 'tasks'

    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        tasks=context.get('object_list')
        context['tasks']= tasks
        return context



class TaskUpdate(UpdateView):
    model = Task
    template_name = 'task/taskcreate.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasklist')


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'task/deleteconfirmation.html'
    success_url = reverse_lazy('tasklist')


class TaskDetails(DetailView):
    model = Task
    template_name = 'task/taskdetail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'