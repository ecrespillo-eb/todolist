from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Todo, Priority
from django.urls import reverse_lazy


class CreateTodoView(CreateView):
    model = Todo
    fields = ['description', 'done', 'priority']
    success_url = reverse_lazy('list_todo')

    def form_valid(self, form):
        form.instance.assigned_user = self.request.user
        return super().form_valid(form)


class CreatePriorityView(CreateView):
    model = Priority
    fields = '__all__'
    success_url = reverse_lazy('list_todo')


class UpdateAssignedUser(UpdateView):
    model = Todo
    fields = ['assigned_user']
    success_url = reverse_lazy('list_todo')


class UpdateTodoView(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list_todo')


class DeleteTodoView(DeleteView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list_todo')


class ListTodoView(ListView):
    model = Todo
    paginate_by = 100
    fields = '__all__'
    success_url = reverse_lazy('list_todo')
