from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def index(request):
    notes = Note.objects.all().order_by('-created_at')
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'notes/index.html', {'form': form, 'notes': notes})
