from cmath import e
import email
from email.mime import image
from http.client import EXPECTATION_FAILED
from multiprocessing import context
from urllib import request
from urllib.request import Request
from warnings import catch_warnings
from django.shortcuts import redirect, render
from django.views.generic import ListView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from hopital.settings import BASE_DIR
from hopitall.models import NewUser,Formulaire


from .forms import CreateUserForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from hopitall.detection import FaceRecognition
from django.contrib.auth import authenticate, login

faceRecognition = FaceRecognition()

csp = str(BASE_DIR)

def appointements(request,id):
   appointement= Formulaire.objects.all()
   

   return render(request,'appointements.html',{'appointement':appointement})

def profile(request,id):
    try:
        user=NewUser.objects.filter(id=id).first()

    
        if request.method == 'POST':
            try:
                
              
                user.user_update(full_name=request.POST['fullname'],email = request.POST['email'],user_name=request.POST['username'],password=request.POST['password'])
           
                
            except Exception as e:
                print(e)

        
        username=user.user_name
        mail=user.email
        fullname=user.full_name
        isdocter=user.is_doctor
        print(isdocter)
        img=user.img
        url=csp+"/mediafiles/"+str(img)
        user1={'username':username,'mail':mail,'fullname':fullname,'docter':isdocter,'img':img,'id':str(id)}
        return render(request, 'profile.html',{'user':user1})
    except Exception as e:
                print(e)



def appointment(request,id):
    msg=""
    if request.method == 'POST':
        try:
            fullname = request.POST['fullname']
            print({"alo":fullname})
            email = request.POST['email']
            date = request.POST['date']
            departement =request.POST['departement']
            message =request.POST['message']
            f=Formulaire(name=fullname,email=email,date=date,departement=departement,message=message)
            f.save()
            if f:
                msg="User created"
            
        except Exception as e:
            print(e)

    return render(request, 'appointment.html',{"msg":msg})

def login_cam():
    print("test")
    face_id = faceRecognition.recognizeFace()
    print(type(face_id))
    return face_id

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def login_sign(request):
    user = User()

    if request.method == 'POST':      
        if 'signup' in request.POST:
            serializer = RegistrationSerializer(data=request.POST)
            if serializer.is_valid():
                account = serializer.save(image=request.FILES['img'])
                id=account.id
                print(id)
                addFace(id)
            else:
                data = serializer.errors
                print(data)
        elif 'signin' in request.POST:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    user=NewUser.objects.filter(user_name=username).first()
              

                    return redirect('authentification/'+str(user.id))
                   
              
                   

    return render(request, 'login_sign.html', {})

 
def addFace(face_id):
    face_id = face_id
    print(face_id)
    faceRecognition.faceDetect(face_id)
    print("detection")
    faceRecognition.trainFace()
    print("train")
    return redirect('/')



def authentification(request,id):
    if request.method == 'POST': 
        login_cam()
        return redirect('profile/'+str(id))       

    return render(request, 'authentification.html', {})        

