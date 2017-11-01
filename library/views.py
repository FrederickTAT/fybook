from django.shortcuts import render
from .models import Book
from django import forms
from django.http import HttpResponse,JsonResponse
# Create your views here.

class bookForm(forms.Form):
    title = forms.CharField(max_length=20)
    author = forms.CharField(max_length=20)
    seller = forms.CharField(max_length=20)
    price = forms.FloatField(max_value=3)
    description = forms.TextInput()

def library(request):
    return render(request,'library.html')

def append(request):
    if request.method=='POST':
        bookfm=bookForm(request.POST)
        book_id=Book.objects.create(title=bookfm.title,author=bookfm.title,seller=bookfm.seller,price=bookfm.price,description=bookfm.description).id
        return HttpResponse(book_id)

def remove(request):
    if request.method=='POST':
        getbook=Book.objects.get(id=request.POST.get('id'))
        if getbook:
            getbook.delete()
            return HttpResponse(1)
        else:
            return HttpResponse(0)

def search(request):
    if request.method=="GET":
        type=request.GET.get('type')
        content=request.GET.get('content')
        re=request.GET.get('re')

        if type == 'id':
            result=Book.objects.filter(id=content)
        elif type == 'title':
            result=Book.objects.filter(title__icontains=content)
        elif type == 'author':
            result=Book.objects.filter(author_icontains=content)
        elif type == 'seller':
            result=Book.objects.filter(seller_icontains=content)
        elif type == 'description':
            result=Book.objects.filter(description__icontains=content)

        if re=='all':
            return JsonResponse(list(result.values()))
        else:
            relist=[]
            for comb in list(result.values(re)):
                relist.append(comb[re])
            return JsonResponse(relist)




