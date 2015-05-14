from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from attorney.models import Attorney, LawCategory, ServiceArea


class AttorneyDetailView(DetailView):
    model = Attorney

    def get_context_data(self, **kwargs):
        context = super(AttorneyDetailView, self).get_context_data(**kwargs)
        return context


class AttorneyListView(ListView):
    model = Attorney

    def get_queryset(self):
        queryset = None

        area_id = int(self.kwargs.get('area_id', 0))
        cat_id = int(self.kwargs.get('cat_id', 0))
        if cat_id > 0:
            queryset = Attorney.objects.filter(service_areas__id=area_id, categories__id=cat_id)
        else:
            queryset = Attorney.objects.filter(service_areas__id=area_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(AttorneyListView, self).get_context_data(**kwargs)
        context['categories'] = LawCategory.objects.all()
        context['areas'] = ServiceArea.objects.all()

        # If there is a category selected we need to send it as well
        cat_id = int(self.kwargs.get('cat_id', 0))
        if cat_id > 0:
            context['selected_category'] = LawCategory.objects.get(pk=cat_id)

        # Grab area id
        area_id = int(self.kwargs.get('area_id', 0))
        context['selected_area'] = ServiceArea.objects.get(pk=area_id)

        return context