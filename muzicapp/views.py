from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Muzic


class Homepage(ListView):
    model = Muzic
    template_name = 'index.html'

class Detail(DetailView):
    model = Muzic
    template_name = 'detail.html'



class Create(CreateView):
    model = Muzic
    template_name = 'create.html'
    fields = '__all__'
    success_url = '/'

class Update(UpdateView):
    model = Muzic
    template_name = 'update.html'
    fields = '__all__'
    success_url = '/'


class Delete(DeleteView):
    model = Muzic
    template_name = 'delete.html'
    success_url = '/'