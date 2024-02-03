from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):

    return HttpResponse('Welcome to 6410742446 Phatchara Rakchuai views!')

def item_view(request,item_id):

    context_data = {
        "item_id":item_id,
    }

    return render(request,'index.html',context=context_data)

def homepage_view(request):
    return render(request,'home.html')

def category_view(request):
    return HttpResponse("My Category")

def product_view(request):
    return HttpResponse("My Product")

def checkout_view(request):
    return HttpResponse("My Checkout")

def contact_page(request):
    return HttpResponse("My Contact")