from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View

class Home(View):

    def get(self, request):

        return render(self.request, 'home.html')