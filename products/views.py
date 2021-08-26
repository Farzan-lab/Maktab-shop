from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    paginate_by = 10
    template_name = "products/home.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('category'):
            context['category'] = self.request.GET.get('category')
            context['categories'] = Category.objects.filter(parent__name=self.request.GET.get('category'))
        else:
            context['categories'] = Category.objects.filter(parent=None)
        context["home"] = True
        return context

    def get_queryset(self):
        if self.request.GET.get('category'):
            categories = Category.objects.get(name=self.request.GET.get('category')).get_children()
            category_ids = [cat.id for cat in categories]
            queryset = Product.objects.filter(category__id__in=category_ids)
        else:
            queryset = Product.objects.all()

        return queryset
        
class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product-detail.html"