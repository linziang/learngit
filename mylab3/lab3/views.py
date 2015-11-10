from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from models import *
def search(request):  
    word = ""    
    if request.POST:
        word = request.POST["word"]
        p = Author.objects.get(Name = word)
        q = Book.objects.filter(AuthorID = p)
        #c = Context({"result_list":result_list,"result_len":len(result_list)})
        return render_to_response("result.html",{'result_list':q,'result_len':len(q)})
    return HttpResponseRedirect("/show/")
    
def show(request):
    Book_list = Book.objects.all()
    c = Context({"Book_list":Book_list})
    return render_to_response("show.html",c)

def delete(request):
    dltid = request.GET["id"]
    if len(Book.objects.filter(id=dltid)) > 0:
        Book.objects.filter(id=dltid).delete()
        return HttpResponseRedirect("/show/")
        
def click(request):
    clid = request.GET["id"]
    p = Book.objects.get(id=clid)
    q = p.AuthorID
    c = Context({"book":p,"author":q})
    return render_to_response("click.html",c) not really good!