from django.shortcuts import render # type: ignore
from rest_framework import viewsets # type: ignore
from .models import Note
from .serializers import NoteSerializer

class NotesViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer  # Update to the correct serializer name

