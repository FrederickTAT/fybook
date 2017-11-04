from django.shortcuts import render
from .models import Book,Comment
from django import forms
from django.http import HttpResponse,JsonResponse
# Create your views here.


class BookForm(forms.Form):
    title = forms.CharField(max_length=20)
    author = forms.CharField(max_length=20)
    seller = forms.CharField(max_length=20)
    price = forms.FloatField(max_value=3)
    description = forms.TextInput()


class CommentForm(forms.Form):
    bookid = forms.IntegerField()
    user = forms.CharField(max_length=20)
    time = forms.DateTimeField()
    content = forms.TextInput()
    rank = forms.IntegerField()



def library(request):
    return render(request,'library.html')


def book_add(request):
    if request.method=='POST':
        bookfm=BookForm(request.POST)
        book_id=Book.objects.create(title=bookfm.title,author=bookfm.title,seller=bookfm.seller,price=bookfm.price,description=bookfm.description).id
        return HttpResponse(book_id)


def book_remove(request):
    if request.method=='POST':
        getbook=Book.objects.get(id=request.POST.get('id'))
        if getbook:
            getbook.delete()
            return HttpResponse(1)
        else:
            return HttpResponse(0)


def book_search(request):
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

        if result:
            if re=='all':
                return JsonResponse(list(result.values()),safe=False)
            else:
                relist=[]
                for comb in list(result.values(re)):
                    relist.append(comb[re])
                return JsonResponse(relist,safe=False)
        else:
            return JsonResponse([])


def comment_add(request):
    if request.method=='POST':
        ComFm=CommentForm(request.POST)
        Comment.objects.create(bookid=ComFm.bookid,user=ComFm.user,time=ComFm.time,content=ComFm.content,rank=ComFm.rank)
        return HttpResponse(1)

def comment_remove(request):
    if request.method=='POST':
        getcm=Comment.objects.filter(bookid=request.POST['bookid'],user=request.POST['user'])
        if getcm:
            getcm.delete()
            return HttpResponse(1)
        else:
            return HttpResponse(0)

def comment_search(request):
    if request.method=='GET':
        getcmlist=list(Comment.objects.filter(bookid=request.GET.get('bookid')).values())
        if getcmlist:
            for cmt in getcmlist:
                cmt['time']=str(cmt['time'])[:19]
            return JsonResponse(getcmlist,safe=False)

        else:
            return JsonResponse([],safe=False)



