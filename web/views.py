from django.shortcuts import render
from product.models import Product

# Create your views here.
def home(request):
    product= Product .object.all()
    return render(request, template_name="web/home.html", context:{"products":products})


