from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.http import Http404

from .models import Notes
# Create your views here.


class NotesView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

