from django.shortcuts import render

def All_Products(request):
    return render(request,"inventory_templates/all_products.html")

