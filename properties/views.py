from django.shortcuts import render, redirect,get_object_or_404
from properties.models import allproperties,Rooms
from formapp.models import Realtors
from properties.forms import PropertiesForm
from properties.forms import PropertyEditForm
from django.core.paginator import Paginator

# Create your views here.


def property_detail(request,id=0): 
    detail = allproperties.objects.get(id=id) 
     
    return render(request, "properties/property_details.html", {'detail':detail} )


def dashboard_details(request):
    
    realtors=Realtors.objects.filter(user=request.user).first()
    details = allproperties.objects.filter(realtorname=realtors)
    if realtors:
        paginator = Paginator(details,2)
        page = request.GET.get('pg')
        page_obj= paginator.get_page(page)


        
    
    else:
        details= []
    return render(request, "realtors/dashboard.html", {
            'page_obj': page_obj,
            'realtors': realtors
        })

# @login_required(login_url="login")
# def dashboard_details(request):
#     user = request.user
#     realtor = Realtors.objects.filter(user=user).first()

#     if realtor:
#         properties = allproperties.objects.filter(realtorname=realtor)
#         paginator = Paginator(properties,1)
#         page = request.GET.get('pg')
#         # properties = Paginator.get_page(page)
    
#     else:
#         properties= []

#     return render(request, 'realtors/dashboard.html',{'properties':properties,
#       'realtor':realtor})


def add_new_property(request):
    if request.method=='POST':
        form = PropertiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('dashboard')
        else:
            print(form.errors)   
    else:
        form=PropertiesForm()
    return render(request, 'properties/add_property.html', {'form':form})


def propertyEdit(request,id=0):

    proper = get_object_or_404(
        allproperties,
        id=id

    )
    

    form = PropertyEditForm(
        instance=proper
    )

    if request.method    == 'POST':

        form = PropertyEditForm(

            request.POST,
            request.FILES,
            instance=proper
        )


        if form.is_valid():

            form.save()

            return redirect('dashboard')


    return render(request,
                  'properties/property_edit.html',
                  {'form':form})



    # if request.method == 'POST':

    #     form = Pr


def buy(request, id ):

    details_this = allproperties.objects.get(id=id)
    

    return render(request,'properties/buy.html')

