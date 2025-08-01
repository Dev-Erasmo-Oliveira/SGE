from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms

class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflows_list.html'
    context_object_name = 'inflows'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset
    

class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflows_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflows_list')


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflows_detail.html'


    
