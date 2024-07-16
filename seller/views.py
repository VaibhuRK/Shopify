from django.shortcuts import render,redirect
from django.http import HttpResponse
from seller.models import Product
from django.contrib.auth.models import User


# Create your views here.
def dashboard(request):
    if(request.user.is_authenticated):
       return render(request,'seller/dashboard.html')
    else:
        return redirect("/")
    
def add_product(request):
     if(request.method=='POST'):
      name=request.POST.get('name')
      price=request.POST.get('price')
      description=request.POST.get('description')
      quantity=request.POST.get('quantity')
      category=request.POST.get('category')
      image=request.FILES.get('image')
      is_available=request.POST.get('is_available') and ('is_available' in request.POST)
      # print(is_available in request.POST)
      # print(name,price,description,quantity,category,is_available)
      user_id=request.user.id
      user=User.objects.get(id=user_id)
      created_product=Product.objects.create(name=name,price=price,category=category,description=description,quantity=quantity,is_active=is_available,image=image,sid=user)
      created_product.save()
      return redirect("/dashboard")
     return render(request,'seller/add_product.html')

def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    print(product)
    product.delete()
    return redirect("/dashboard")

def update_product(request,product_id):
    data={}
    product=Product.objects.filter(id=product_id)
    print(product) #queryset
    print(product[0]) #only one object as in cmd it returns a list
    data['product']=product[0]

    if request.method=='POST':
      name=request.POST.get('name')
      price=request.POST.get('price')
      description=request.POST.get('description')
      quantity=request.POST.get('quantity')
      category=request.POST.get('category')
      is_available= 'is_available' in request.POST

     
      products=Product.objects.filter(id=product_id)

      products.update(name=name,price=price,category=category,description=description,quantity=quantity,is_active=is_available)
     
      product=Product.objects.get(id=product_id)
      from seller.forms import ImageForm
      import os
      form=ImageForm(request.POST, request.FILES,instance=product)
      if form.is_valid():
         image_path=product.image.path
         if(os.path.exists(image_path)):
            os.remove(image_path)
         form.save()
      return redirect('/dashboard/products')
    return render(request,"seller/update_product.html",context=data)

def view_products(request):
    data={}
    products=Product.objects.filter(sid=request.user.id)
    data['products']=products
    return render(request,'seller/products.html',context=data)
