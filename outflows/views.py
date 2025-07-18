from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms

class OutflowListView(ListView):
    model = models.Outflows
    template_name = 'outflows_list.html'
    context_object_name = 'outflows'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset
    

class OutflowCreateView(CreateView):
    model = models.Outflows
    template_name = 'outflows_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflows_list')


class OutflowDetailView(DetailView):
    model = models.Outflows
    template_name = 'outflows_detail.html'


    
