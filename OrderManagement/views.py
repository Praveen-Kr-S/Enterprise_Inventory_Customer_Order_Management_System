from django.shortcuts import render,redirect
from .models import Orders,Products,Customers
from .forms import OrderForm

def All_Orders(request):
    orders = Orders.objects.all()
    return render(request,'OrderManagement/allorders.html', {'orders': orders})


def Add_Order(request):
    order_form = OrderForm()

    if request.method == 'POST':
        # print(request.POST)
        product_reference = Products.objects.get(id=request.POST.get('product_reference'))
        amount = float(product_reference.price)*float(request.POST.get('quantity'))
        gst = float(amount*product_reference.gst)/100
        bill_amount = amount+gst

        new_order = Orders(
            product_reference_id = request.POST.get('product_reference'),
            customer_reference_id = request.POST.get('customer_reference'),
            order_number = request.POST.get('order_number'),
            order_date = request.POST.get('order_date'),
            quantity = request.POST.get('quantity'),
            amount = amount,
            gst = gst,
            bill_amount = bill_amount
        )

        new_order.save()
        return redirect('allorders')




    return render(request, 'OrderManagement/add_and_edit_order.html', {'order_form': order_form})


def Update_Order(request, pk):
    order = Orders.objects.get(id=pk)
    edit_order_form = OrderForm(instance=order)

    if request.method == 'POST':
            # print(request.POST)
            product_reference = Products.objects.get(id=request.POST.get('product_reference'))
            amount = float(product_reference.price)*float(request.POST.get('quantity'))
            gst = float(amount*product_reference.gst)/100
            bill_amount = amount+gst

            filter_order = Orders.objects.filter(id=pk)
            filter_order.update(
                product_reference_id = request.POST.get('product_reference'),
                customer_reference_id = request.POST.get('customer_reference'),
                order_number = request.POST.get('order_number'),
                order_date = request.POST.get('order_date'),
                quantity = request.POST.get('quantity'),
                amount = amount,
                gst = gst,
                bill_amount = bill_amount
            )
            return redirect('allorders')

    return render(request, 'OrderManagement/add_and_edit_order.html', {'edit_order_form': edit_order_form})



def Delete_Order(request, pk):
    order = Orders.objects.get(id=pk)
    order.delete()
    return redirect('allorders')