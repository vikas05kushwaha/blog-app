from ctypes.wintypes import HACCEL
from django.shortcuts import render 
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from httplib2 import Http
from home.models import  Contact,Blog,Tag ,cats
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from home.forms import BlogFrom,TagForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json


# Create your views here.
def index(request):
    
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        if(request.GET.get('tag')!=None):
            tag=request.GET.get('tag', 1)
            blog=Blog.objects.filter(tags__in=[tag])
        else:
            
            blog=Blog.objects.all()   
                #pagination
        page=request.GET.get('page',1)
        paginator=Paginator(blog,3)
        try:
            blog=paginator.page(page)
        except PageNotAnInteger:
            blog=paginator.page(1)
        except EmptyPage:
            blog=paginator.page(paginator.num_pages)


        context={
            
            'blogs':blog,
              }

        return render(request,'index.html',context)
    

def contact(request):
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        # return render(request,'contact.html')    
        if (request.method=='POST'):
                name=request.POST['name']
                email=request.POST['email']
                phone=request.POST['phone']
                desc=request.POST['desc']
                contact=Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
                contact.save()  
    return render(request,'contact.html')  
            # return HttpResponse("this is contact page")

def loginUser(request):
     if(request.method=="POST"):
         username=request.POST['username']
         password=request.POST['password']

         user=authenticate(username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect("/")

         else:
              return render(request,'login.html')
     return render(request,'login.html')

def logoutUser(request):
     logout(request)
     return redirect('/login')

def blogpost(request,idd):
    # if(request.user.is_anonymous):
    #     return redirect("/login")
    # else:
        blogpost=Blog.objects.get(id=idd)
        # contact.name="Test"
        # contact.save()
        context={
                'blogpost':blogpost
            } 
        # return render(request,'contact.html') 
        return render(request,'blogpost.html',context)  
def blogs(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        if (request.method=='POST'):
            title=request.POST['title']
            username=request.POST['username']
            userid=request.POST['userid']
            description=request.POST['description']
            tags=request.POST['tag']
            blogs=Blog(tags=tags,title=title,description=description,username=username,userid=userid)
            blogs.save() 
        return render(request,'blogform.html') 

# def blogs(request):
#     if(request.user.is_anonymous):
#         return redirect('/login')
#     else:
#         form=BlogFrom()
#         if(request.method == 'POST'):
#             form=BlogFrom(request.POST,request.FILES)
#             # print(form.fields.get('image'))
#             # form.fields.get('title')
#             if(form.is_valid()):
#                 print("validated")
#                 form.save()
#                 messages.add_message(request, messages.INFO, 'This is done')
                
#             else:
                
#                 print(form.errors)
#                 messages.add_message(request, messages.INFO, 'some error ')
#             return render(request,'blogform.html')    
#         else: 
#             context={
#                   'form':form
#                   }       
#             return render(request, 'blogform.html',context) 




def tag(request):
    if (request.method=='POST'):
        Title=request.POST['Title'] 
        tag =Tag(Title=Title)  
        tag.save()
    return render(request,'tag.html') 

def about(request):
    if(request.user.is_anonymous):
        return redirect('/login')      


def blogpostupdate(request,idd):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        blogs=Blog.objects.get(id=idd)
        form=BlogFrom(initial={'userid':request.user.id,'username':request.user.username,'title':blogs.title,'description':blogs.description,'image':blogs.image,'date':blogs.date,'tags':blogs.tags.all})
        if(request.method == 'POST'):
            # request.POST['user_id']=request.user.id
            form=BlogFrom(request.POST,request.FILES,instance=blogs)
            # form.data['user_id']=request.user.id
            print("filed form",form['userid'].value())
            form.errors.as_data()
            if(form.is_valid()):
                print("validated")
                form.save()
                messages.add_message(request, messages.INFO, 'success')
            else:
                print("error")
                errors=form.errors.as_json()
                print(errors)
                # errors = json.loads(errors)
                # message=errors["userid"]
                # message = json.loads(message)
                # print(message)
                
                messages.add_message(request, messages.INFO, 'failed')
        
        
        context={
                'form':form,
                'id':idd
            }
        return render(request, 'blogupdate.html',context)


def blogpostdelete(request,idd):
    blogs=Blog.objects.get(id=idd)
    blogs.delete()
    return redirect("/index")
def about(request):
    return HttpResponse("This is an about page")

# def ana(request):
#     ana=cats.objects.all()
#     for i in ana:
#        print("name=" + i.name , "Owner="+ i.owner)
#     return HttpResponse(ana)
       

def track(request):
    track=cats.objects.all()
    for i in track:
       print(i.name)
       print(i.owner)
    return HttpResponse(track) 


# def staff(request):
#     staff=Staff.objects.all()
#     for i in staff:
#        print(i.fullname)
#        print(i.mobile)
#     return HttpResponse(staff) 
    

def blogform(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    else:
        form=BlogFrom(initial={'userid':request.user.id,'username':request.user.username})
        if(request.method == 'POST'):
            # request.POST['user_id']=request.user.id
            form=BlogFrom(request.POST,request.FILES)
            # form.data['user_id']=request.user.id
            print("filed form",form['userid'].value())
            form.errors.as_data()
            if(form.is_valid()):
                print("validated")
                form.save()
                messages.add_message(request, messages.INFO, 'success')
            else:
                
                errors=form.errors.as_json()
                
                messages.add_message(request, messages.INFO, 'failed')
        
        
        context={
                'form':form
            }
        return render(request,'blogform.html',context)
              
           
