from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import NotesForm
from .models import Notes
# Create your views here.


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
