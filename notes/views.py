from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm
from .models import Notes
# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url='/smart/notes'

class NotesView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url='/smart/notes'

