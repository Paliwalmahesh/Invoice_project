from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
from .models import Invoice,Items
from django.views.generic import CreateView

def add_invoice(request):
    unique_id = get_random_string(length=10)
    temp = unique_id
    if request.method=="POST":
        Invoice_Id = temp
        if Invoice.objects.filter(Invoice_Id=Invoice_Id).exists():
            return render(request,'posts/getInvoice_add',{'Invoice_Id':Invoice_Id}, {'i':'Test ID Already exists! Try Again!!'}) 
        else:
            Invoice_add = Invoice(Invoice_Id=Invoice_Id)
            Invoice_add.save()
            return redirect("Add_Item",Invoice_Id)      
    else:
        return render(request,'posts/getInvoice_add.html')

def Add_Item(request,Invoice_Id):
    Invoice_Ids = Invoice.objects.get(Invoice_Id=Invoice_Id)
    Items_added=Items.objects.filter(Invoice_no=Invoice_Ids)
    total_cost=0
    if request.method=="POST":
        Cost=request.POST["Cost"]
        description=request.POST["description"]
        item_add=Items(Invoice_no=Invoice_Ids,Cost=Cost,description=description)
        item_add.save()
        
        for i in Items_added:
            total_cost+=i.Cost
     
        context={
        'Item_added':Items_added,
        'Invoice_Id':Invoice_Id,
        'total_cost':total_cost,
        }
        return render(request,'posts/new_item.html',context)

    else:
        return render(request,'posts/new_item.html',{'Invoice_Id':Invoice_Id})
def printi(request):
    pass