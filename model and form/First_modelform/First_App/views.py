from django.shortcuts import render
from django.http import HttpResponse
from First_App.models import First_Table
from First_App.models import Second_table
from First_App import form
from First_App.form import tableform

# Create your views here.
def table(request):
    New_Table=First_Table.objects.order_by("F_Name")
    Old_Table=Second_table.objects.order_by("First_Name")
    diction={'heading_1':'This is first table','First_Table':New_Table,'Second_table':Old_Table,'Second_t':"This is Second Table",'text_sample':"This is table"}
    return render (request, 'table.html', context=diction)
def form_contact(request):
    new_form=form.tableform()
    
    if request.method == "POST":
        new_form=form.tableform(request.POST)
        
        if new_form.is_valid():
        
            new_form.save(commit=True)   
            
            return table(request)

    old_form=form.secondform()
    if request.method == "POST":
       old_form=form.secondform(request.POST)

       if old_form.is_valid():
          old_form.save(commit=True)
          return table(request)
    diction={'text_form':new_form,'text2_form':old_form}
    return render(request,'form.html', context=diction)