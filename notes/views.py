from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView
from .models import Notes
from .forms import NotesForm
# Create your views here.

class NotesListView(ListView):
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


