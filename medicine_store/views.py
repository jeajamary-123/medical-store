from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import ProductForm ,MedicineSearchForm
from .models import med_kit
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('create')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

    return render(request,'home_page.html')
    

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieve')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})
def retrieve_items(request):
    data = med_kit.objects.all()
    return render(request,'retrieve.html',{'data':data})
def product_update(request, id):
    product = med_kit.objects.get(pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieve')  # Redirect to the product list or another desired page
    else:
        form = ProductForm(instance=product)

    return render(request, 'update.html', {'form': form, 'product': product})

def product_delete(request,id):
    product=med_kit.objects.get(pk=id)  
    if request.method == 'POST':
        product.delete()
        return redirect('retrieve')
    
    return render(request,'delete.html',{'product':product})

def search_medicine(request):
    if request.method == 'GET':
        form = MedicineSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            medicines = med_kit.objects.filter(Medname__icontains=search_query)
            return render(request, 'search_results.html', {'medicines': medicines, 'query': search_query})
    else:
        form = MedicineSearchForm()
    return render(request, 'search_form.html', {'form': form})