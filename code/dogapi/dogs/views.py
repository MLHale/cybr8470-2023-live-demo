# @Author: Matthew Hale <mlhale>
# @Date:   2023-09-11T18:20:06-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: views.py
# @Last modified by:   mlhale
# @Last modified time: 2023-09-18T18:29:47-05:00
# @Copyright: Copyright (C) 2019 Matthew L. Hale



from django.shortcuts import render
from django.http import HttpResponse
from dogs.models import Dog
from rest_framework import viewsets
from rest_framework import serializers

def index(request):
    return HttpResponse("Hello, world.")
    

class DogSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=40)
    breed = serializers.CharField(max_length=40)

class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
