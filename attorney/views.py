from django.shortcuts import render,redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, TemplateView, View
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

        area_id = int(self.get_param('area_id', 1))
        cat_id = int(self.get_param('cat_id', 0))
        if cat_id > 0:
            queryset = Attorney.objects.filter(service_areas__id=area_id, categories__id=cat_id)
        else:
            queryset = Attorney.objects.filter(service_areas__id=area_id)

        return queryset

    def get_param(self, key, default):
        value = default
        if key in self.request.GET:
            value = self.request.GET[key]
        elif key in self.kwargs:
            value = self.kwargs[key]
        return value

    def get_context_data(self, **kwargs):
        context = super(AttorneyListView, self).get_context_data(**kwargs)
        context['categories'] = LawCategory.objects.all()
        context['areas'] = ServiceArea.objects.all()

        # If there is a category selected we need to send it as well
        cat_id = int(self.kwargs.get('cat_id', 0))
        if cat_id > 0:
            context['selected_category'] = LawCategory.objects.get(pk=cat_id)

        # Grab area id
        area_id = int(self.kwargs.get('area_id', 1))
        context['selected_area'] = ServiceArea.objects.get(pk=area_id)

        return context

class IndexPageView(View):

    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = {'categories': LawCategory.objects.all(), 'areas': ServiceArea.objects.all()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        category_id = self.request.POST.get("category_id", 1)
        area_id = self.request.POST.get("area_id", 1)

        return redirect("attorney_list_cat", area_id=area_id, cat_id=category_id, permanent=True)