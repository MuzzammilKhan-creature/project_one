from django.shortcuts import render
from .froms import productform
from django.http import HttpResponse 





def add_product (request):
    from =
ProductForm(request.POST)
    if form.is_valid():
      form.save()

   return render(request, 'add_product.html',{'form': form})
