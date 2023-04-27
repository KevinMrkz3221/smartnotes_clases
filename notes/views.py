from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http.response import HttpResponseRedirect

from .forms import NotesForm
from .models import Notes
# Create your views here.

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url='/smart/notes'
    login_url = '/login'

class NotesView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    login_url = '/login'


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = '/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NotesForm
    success_url='/smart/notes'
    login_url = '/login'

