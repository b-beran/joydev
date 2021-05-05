from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io


@staff_member_required
def admin_order_pdf(request, order_id):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(100, 100, "hello world")

    p.showPage()
    p.save()

    buffer.seek(0)
    order = get_object_or_404(Order, id=order_id)
    # return render(request, 'admin/orders/order/detail.html', {'order': order})
    return FileResponse(buffer, as_attachment=True, filename='order.pdf')


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         note=item['note'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
