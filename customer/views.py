from django.http import Http404
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .forms import CustomerForm
from .models import *

# Create your views here. Arrange Views in alphabetical order
class MainIndexView(View):
    def get(self, request):
        # print('get')
        return render(request, 'customer/mainIndex.html')
    
class CustomerIndexView(View):
    def get(self, request):
        customers = Customer.objects.all()
        context = {
                'customers' : customers
            }
        return render(request, 'customer/index.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print('update profile button clicked')
                sid = request.POST.get("customer-id")
                #   date = request.POST.get("date-registered")
                fname = request.POST.get("customer-fname")
                mname = request.POST.get("customer-mname")
                lname = request.POST.get("customer-lname")
                address = request.POST.get("customer-address")
                birthdate = request.POST.get("customer-bdate")
                birthplace = request.POST.get("customer-bplace")
                  # gender = request.POST.get("gender")
                  # status = request.POST.get("status")
                  # email = request.POST.get("email")
                  # password = request.POST.get("password")
                print(birthplace)
                update_customer = Customer.objects.filter(person_ptr_id = sid).update(firstname = fname, middlename = mname, lastname = lname, address =address,
                                          birthdate = birthdate, birthplace = birthplace)
                print(update_customer)
                print('profile updated')
            elif 'btnDelete' in request.POST:   
                print('delete button clicked')
                sid = request.POST.get("customer-id")
                cust = Customer.objects.filter(person_ptr_id=sid).delete()
                pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
        return HttpResponse ('post')
        #return redirect('customer:customer_index_view')
        #for customer in customers:
         #   print(customer)
          #  print(customer.id)
           # print(customer.firstname)
            #print(customer.lastname)
          #  print(customer.birthdate)
          #  print(customer.address)
             
class CustomerRegisterView(View):
    def get(self, request):
    	# print('get')
    	return render(request, 'customer/registration.html')
    def post(self, request):        
        form = CustomerForm(request.POST)        
        # fname = request.POST.get("firstname")
        # print(fname)
        # lname = request.POST.get("lastname")
        # print(lname)
        if form.is_valid():
            # try:
            date = request.POST.get("date_registered")
            fname = request.POST.get("firstname")
            mname = request.POST.get("middlename")
            lname = request.POST.get("lastname")
            address = request.POST.get("address")
            birthdate = request.POST.get("birthdate")
            birthplace = request.POST.get("birthplace")
            gender = request.POST.get("gender")
            status = request.POST.get("status")
            email = request.POST.get("email")
            password = request.POST.get("password")
            print(email)
            form = Customer(date_registered = date, firstname = fname, middlename = mname, lastname = lname, address =address,
                                  birthdate = birthdate, birthplace = birthplace, gender = gender, status = status, email = email , password = password)
            form.save()

            return HttpResponse('Customer record saved!')            
            # return render(request,'successpage.html')
            # except:
            #   raise Http404
        else:
            print(form.errors)
            return HttpResponse('not valid')