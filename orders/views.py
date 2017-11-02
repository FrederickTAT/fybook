from django.shortcuts import render
from .models import Order
from django.http import HttpResponse,JsonResponse
from django import forms
# Create your views here.

class OrderForms(forms.Form):
    book_id=forms.IntegerField()
    customer=forms.CharField(max_length=20)

def create_order(request):
    if request.method=='POST':
        of=OrderForms(request.POST)
        if not Order.objects.get(book_id=OrderForms.book_id):
            Order.objects.create(book_id=OrderForms.book_id,customer=OrderForms.customer,dealt=True)
            return HttpResponse(1)
        else:
            return HttpResponse(0)

def del_order(request):
    if request.method=='POST':
        get_order=Order.objects.get(id=request.POST['id'])
        if get_order:
            get_order.delete()
            HttpResponse(1)
        else:
            HttpResponse(0)

def get_order(request):
    if request.method=='GET':
        get_order_q=Order.objects.filter(id=request.GET['id'])
        if get_order_q:
            get_order=get_order_q[0]
            ordertime=str(get_order['ordertime'])[:19]
            get_order['ordertime']=ordertime
            return JsonResponse(get_order)
        else:
            return JsonResponse({})

def make_deal(request):
    if request.method=='POST':
        get_order=Order.objects.filter(id=request.GET['id'])
        if get_order:
            if get_order.values()[0]['dealt']:
                return HttpResponse(2)
            else:
                get_order.update(dealt=True)
                return HttpResponse(1)
        else:
            return HttpResponse(0)


def cancel_deal(request):
    if request.method == 'POST':
        get_order = Order.objects.filter(id=request.GET['id'])
        if get_order:
            if get_order.values()[0]['dealt']:
                get_order.update(dealt=False)
                return HttpResponse(1)
            else:
                return HttpResponse(2)

        else:
            return HttpResponse(0)
