from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from attorney.models import Attorney


class AttorneyDetailView(DetailView):

    model = Attorney

    def get_context_data(self, **kwargs):
        context = super(AttorneyDetailView, self).get_context_data(**kwargs)
        return context