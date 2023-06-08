from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .models import Product, ProductType
from .forms import ProductForm

# Create your views here.


class ProductsView(View):
    def get(self, request):
        return render(request, 'list_products.html', {'products': Product.objects.all(),
                                                      'product_form': ProductForm})

    def post(self, request):
        if request.method == 'POST':
            product_form = ProductForm(request.POST)
            if 'btn_save_changes' in request.POST:
                product_name = product_form['product_name'].value().upper()
                model = product_form['model'].value().upper()
                year = product_form['year'].value()
                products = Product.objects.filter(product_name=product_name,
                                                  model=model,
                                                  year=year)
                product = Product.objects.get(id=int(request.POST.get('product_id')))
                if len(products) <= 1 and products[0].id == product.id:
                    product.product_name = product_form['product_name'].value().upper()
                    product.model = product_form['model'].value().upper()
                    product.type = ProductType.objects.get(id=int(product_form['type'].value()))
                    product.year = product_form['year'].value()
                    product.price = product_form['price'].value()
                    product.save()
                else:
                    message = f'No se ha guardado el registro.\n{product_name} {model} {year} ya se encuentra registrado en el sistema.'
                    messages.info(request, message)
            if 'btn_delete' in request.POST:
                product = Product.objects.get(id=int(request.POST.get('product_id')))
                product.delete()
            if 'btn_save' in request.POST:
                if product_form.is_valid():
                    product_name = product_form['product_name'].value().upper()
                    model = product_form['model'].value().upper()
                    year = product_form['year'].value()
                    products = Product.objects.filter(product_name=product_name,
                                                      model=model,
                                                      year=year)
                    if len(products) == 0:
                        product_instance = product_form.save(commit=False)
                        product_instance.product_name = product_name
                        product_instance.model = model
                        product_instance.save()
                    else:
                        message = f'No se ha guardado el registro.\n{product_name} {model} {year} ya se encuentra registrado en el sistema.'
                        messages.info(request, message)
            return redirect(request.META['HTTP_REFERER'])
