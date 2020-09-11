from django.shortcuts import render
from cbApp.models import beer
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView

# Create your views here.
class beerListView(ListView):
    model = beer

class beerDetailView(DetailView):
    model = beer

class beerCreateView(CreateView):
    model = beer
    fields = '__all__'
class beerUpdateView(UpdateView):
    model = beer
    fields = ('taste','color','price')

