from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_api/person_list.html', {'people': people})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'person_api/person_detail.html', {'person': person})
