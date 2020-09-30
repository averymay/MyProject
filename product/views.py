from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .forms import ProductForm
from .models import *

# Create your views here. Arrange Views in alphabetical order
class ProductIndexView(View):
    def get(self, request):
        products = Product.objects.all()
        print(products)
        context = {
            'products' : products
        }
        return render(request, 'product/index.html',context)
    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                pid = request.POST.get("id")
                date = request.POST.get("ndate_registered")
                sku = request.POST.get("nsku")
                cat = request.POST.get("ncategory")
                name = request.POST.get("nname")
                brand = request.POST.get("nbrand")
                color = request.POST.get("ncolor")
                size = request.POST.get("nsize")
                price = request.POST.get("nprice")
                stock = request.POST.get("nstocks")
                img1 = request.POST.get("nimage1")
                img2 = request.POST.get("nimage2")
                img3 = request.POST.get("nimage3")
                update_product = Product.objects.filter(id = pid).update(date_registered = date, sku = sku, category = cat, name = name, brand =brand,
                                  color = color, size = size, price = price, stocks = stock, image1 = img1 , image2 = img2, image3 = img3)
                print(update_product)
                print('profile updated')
            elif 'btnDelete' in request.POST:   
                print('delete button clicked')
                ppid = request.POST.get("pproduct-id")
                prod = Product.objects.filter(id=ppid).delete()
                print('recorded deleted')
        #return HttpResponse ('post')
        return redirect('product:index_view')

class ProductRegisterView(View):
    def get(self, request):
    	# print('get')
    	return render(request, 'product/registration.html')
    def post(self, request):        
        form = ProductForm(request.POST)        
        # fname = request.POST.get("firstname")
        # print(fname)
        # lname = request.POST.get("lastname")
        # print(lname)
        if form.is_valid():
            # try:
            date = request.POST.get("date")
            sku = request.POST.get("sku")
            cat = request.POST.get("category")
            name = request.POST.get("name")
            brand = request.POST.get("brand")
            color = request.POST.get("color")
            size = request.POST.get("size")
            price = request.POST.get("price")
            stock = request.POST.get("stocks")
            img1 = request.POST.get("image1")
            img2 = request.POST.get("image2")
            img3 = request.POST.get("image3")
            print(stock)
            form = Product(date_registered = date, sku = sku, category = cat, name = name, brand =brand,
                                  color = color, size = size, price = price, stocks = stock, image1 = img1 , image2 = img2, image3 = img3)
            form.save()

            return redirect('product:index_view')            
            # return render(request,'successpage.html')
            # except:
            #   raise Http404
        else:
            print(form.errors)
            return HttpResponse('not valid')