from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ProductCreateView(CreateView):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product/create_product.html', context={'form': form})
    
    def post(self, request):
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

class ProductListView(ListView):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'home.html', context={'product': product})


class ProductDetailView(DetailView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'product/product_detail.html', context={'product': product})
    

class ProductUpdateView(UpdateView):
    def get(self, request, pk):
        form = ProductForm()
        return render(request, 'product/product_update.html', context={'form': form})
    
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            product.delete()
            return redirect('home')

      
class ProductDeleteView(DeleteView):
    def get(self, request, pk):
        return render(request, 'product/product_delete.html')
    
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect('home')
