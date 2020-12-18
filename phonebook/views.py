from django.shortcuts import render, redirect
from phonebook.models import PhoneBook
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def index(request,pageNum):
    alluser = PhoneBook.objects.values('id','이름','전화번호')
    alluser = alluser.order_by('-id')
    paging = Paginator(alluser, 2)
    arrPage = []
    for i in range(paging.num_pages):
        arrPage.append(i+1)
    
    context={'유저':paging.page(pageNum),"arrPage":arrPage}
    return render(request, "phonebook/index.html", context)

def add(request):
    if request.method == 'POST':
        table=PhoneBook()
        table.이름=request.POST.get('name')
        table.전화번호=request.POST.get('phNum')
        table.주소=request.POST.get('addr')
        table.이메일=request.POST.get('email')
        table.생년월일=request.POST.get('bir')
        table.작성자=request.POST.get('user')
        table.save()
        return redirect("index",1)
    else:
        return render(request, "phonebook/add.html")
        
def detail(request, userID):
    userInfo = PhoneBook.objects.values('id','이름','전화번호','주소','이메일','생년월일','작성자').get(id=userID)
    context={'userInfo':userInfo}
    if request.user.is_active:
        return render(request, "phonebook/detail.html",context)
    else:
        return redirect("index",1)

def update(request, userID):
    table=PhoneBook.objects.get(id=userID)
    context={'phonebook':table}
    if request.method == 'POST':
        table.이름 = request.POST.get('name')
        table.전화번호 = request.POST.get('phNum')
        table.이메일 = request.POST.get('email')
        table.주소 = request.POST.get('addr')
        table.생년월일 = request.POST.get('bir')
        table.save()
        return redirect("index",1)
    else:
        return render(request, "phonebook/update.html", context)
    
def delete(request, userID):
    table=PhoneBook.objects.get(id=userID)
    table.delete()
    return render(request, "phonebook/delete.html")

def createAccount(request):
    
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST.get('name'),
            email = request.POST.get('email'),
            first_name = request.POST.get('f_name'),
            last_name = request.POST.get('l_name'),
            password = request.POST.get('pwd')
            )
        return redirect('login')
    else: 
        return render(request, "registration/register.html")
    
    
def mainIndex(request):
    return render(request, "subapp/mainIndex.html")

def index2(request):
    return render(request, "subapp/index.html")
    
def page(request, num):
    pbPage = PhoneBook.objects.all()
    paging = Paginator(pbPage , 2)
    context = {'pageNum':paging.page(num) }
    return render(request,'./page.html', context)
    
    
    
    
    
    
    
    
    
    
    

# Create your views here.
