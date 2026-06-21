from django.shortcuts import render,redirect
from formapp.forms import UserForm, UserProfileForm, UserUpdateForm, RealtorForm,UserProfileFormUpdateForm,RealtorProfileForm,EnquiryForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from properties.models import allproperties
from formapp.models import Realtors


from django.db.models import Q

# Create your views here.
def registration(request):
    registered=False
    if request.method=='POST':
        form1=UserForm(request.POST)
        form2=UserProfileForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            
            profile=form2.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        
    else:
        form1=UserForm()
        form2=UserProfileForm()
    context={
        'form1':form1,
        'form2':form2,
        'registered':registered
    }
    return render(request,"registration.html",context)

def user_login(request):
    if request.method=='POST':
        Username=request.POST['username']
        password=request.POST['password']
        # to print in cmd
        # print(username)
        # print(password)
        user=authenticate(username=Username,password=password)
        #//--------------form.username=login.username-----------//
        if user:
            if Realtors.objects.filter(user=user).exists():
                realtor=Realtors.objects.get(user=user)
                if realtor.is_approved:
                    login(request,user) 
                    return redirect("dashboard")
                else:
                    return HttpResponse("realtor not approved")
            else:
                if user.is_active :
                    login(request,user)
                    return redirect('home')
                else:
                    return HttpResponse("User is not active")
        else:
            return HttpResponse("Please check your Credentials")
    return render(request,"login.html")




@login_required(login_url="login")
def home(request):
    properties=allproperties.objects.all()[:5]
    realtor_property=Realtors.objects.all()

    search = request.GET.get('search')

    if search:
        properties = properties.filter(
            name__icontains=search
        )
        print(search)
        print(properties)
        return redirect(f'/homesearch/?search={search}')


    return render(request,"home.html",{'properties':properties,'realtor_property':realtor_property,
   })


@login_required(login_url='login')
def homesearch(request):


    search = request.GET.get('search')

    properties = allproperties.objects.filter(
        Q(name__icontains=search)|
        Q(property_type__icontains=search)|
        Q(price__icontains=search)|
        Q(floors__icontains=search)|
        Q(category__icontains=search)|
        Q(city__icontains=search)|
        Q(name__icontains=search)|
        Q(name__icontains=search)
        
    )

    # form = home.search()

    return render(request,'homesearch.html',{
        'properties': properties
    })

@login_required(login_url='login')
def all_properties(request):
    main = allproperties.objects.all()

    return render(request,'all_properties.html',{'main':main})

@login_required(login_url='login')
def filter_all_properties(request, type):
    if type == 'buy':
        main = allproperties.objects.filter(
            property_type__iexact = type 
        )
        
    elif type == 'rental':
        main = allproperties.objects.filter(
            property_type__iexact = type
        )
    else:
        main = allproperties.objects.all()


    return render(request,'all_properties.html',{'main':main})

    
    

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url="login")
def user_update(request):
    if request.method=="POST":
        form=UserUpdateForm(request.POST,instance=request.user)#newdata ,olddata
        form3=UserProfileFormUpdateForm(request.POST,request.FILES,instance=request.user.userdata)
        if form.is_valid() and form3.is_valid():
            user=form.save()
            user.save()
            
            profile=form3.save(commit=False)
            profile.user=user
            profile.save()
            
            return redirect('profile')
    else:
        form=UserUpdateForm(instance=request.user) 
        form3=UserProfileFormUpdateForm(instance=request.user.userdata)
    return render(request,"update.html",{'form':form,'form3':form3})


def realtor_reg(request):
    registered=False
    if request.method=='POST':
        form3=RealtorForm(request.POST)
        form4=RealtorProfileForm(request.POST,request.FILES)
        if form3.is_valid() and form4.is_valid():
            user=form3.save()
            user.set_password(user.password)
            user.save()
            
            profile=form4.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
        
    else:
        form3=RealtorForm()
        form4=RealtorProfileForm()
    context={
        'form3':form3,
        'form4':form4,
        'registered':registered
    }
    return render(request,"realtorreg.html",context)
    

def realtor_detail(request):
    return render(request, "realtors/realtordetail.html")

def realtor_dashboard(request):
    return render(request, "realtors/dashboard.html")

def enquiry(request):

    submit = False

    form = EnquiryForm()
    # registered=False
    if request.method == 'POST':
        form = EnquiryForm(request.POST)

        if form.is_valid():
            form.save()
            submit =True
            print("enquirs is save")
            
        
    return render(request,'enquiry.html',{'form':form})







