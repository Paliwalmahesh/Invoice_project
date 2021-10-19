from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
from .models import Invoice,Items
from django.views.generic import CreateView
from .forms import ItemsForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


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
		quantity=request.POST["quantity"]
		grand_total=int(quantity)*int(Cost)
		item_add=Items(grand_total=grand_total,Invoice_no=Invoice_Ids,quantity=quantity,Cost=Cost,description=description)
		item_add.save()
		
		for i in Items_added:
			total_cost+=(i.Cost*i.quantity)
	 
		context={
		'Item_added':Items_added,
		'Invoice_Id':Invoice_Id,
		'total_cost':total_cost,
		}
		return render(request,'posts/new_item.html',context)

	else:
		for i in Items_added:
			total_cost+=(i.Cost*i.quantity)
	 
		context={
		'Item_added':Items_added,
		'Invoice_Id':Invoice_Id,
		'total_cost':total_cost,
		}
		return render(request,'posts/new_item.html',context)

def printi(request):
	pass

def updateItems(request, pk):
	items = Items.objects.get(id=pk)
	form = ItemsForm(instance=items)
	if request.method == 'POST':
		Invoice_Id = items.Invoice_no
		form = ItemsForm(request.POST, instance=items)
		if form.is_valid():
			form.save()
			return redirect("Add_Item",Invoice_Id)

	context = {'form':form}
	return render(request, 'posts/Items_form.html', context)

def deleteItems(request, pk):
	item = Items.objects.get(id=pk)
	if request.method == "POST":
		Invoice_Id = item.Invoice_no
		item.delete()
		return redirect("Add_Item",Invoice_Id)

	context = {'item':item}
	return render(request, 'posts/delete.html', context)



def render_pdf_view(request,Invoice_Id):
	Invoice_Ids = Invoice.objects.get(Invoice_Id=Invoice_Id)
	Items_added=Items.objects.filter(Invoice_no=Invoice_Ids)
	total_cost=0
	for i in Items_added:
			total_cost+=(i.Cost*i.quantity)
	Invoice_Ids.total_cost=total_cost
	Invoice_Ids.save()
	template_path = 'posts/Invoice_printer.html'
	context ={
		'Item_added':Items_added,
		'Invoice_Ids':Invoice_Ids,
	}
	# Create a Django response object, and specify content_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	response['Content-Disposition'] = 'filename="report.pdf"'
	# find the template and render it.
	template = get_template(template_path)
	html = template.render(context)

	# create a pdf
	pisa_status = pisa.CreatePDF(html, dest=response)
	# if error then show some funy view
	if pisa_status.err:
	   return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response