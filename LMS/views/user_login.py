from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app.EmailBackEnd import EmailBackEnd

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        #check email
        if User.objects.filter(email=email).exists():
           messages.warning(request,'Email are Already Exists !')
           return redirect('register')
        
        # check username
        if User.objects.filter(username=username).exists():
           messages.warning(request,'Username are Already exists !')
           return redirect('register')
        
        #create user
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        messages.success(request,'Account Created Successfully !')
        return redirect('login')

    return render(request, 'registration/register.html')

	
def DoLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = EmailBackEnd.authenticate(request,username=email,password=password)
        if user != None:
           login(request,user)
           messages.success(request,'Login Successfully !')
           return redirect('home')
        else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
	
    return render(request, 'registration/login.html')


def Logout(request):
    logout(request)
    messages.success(request,'Logout Successfully !')
    return redirect('login')
	   
def Profile(request):
    return render(request, 'registration/profile.html')   
  

def Profile_update(request):
    if request.method == "POST":
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')

      try:
         user = User.objects.get(id=request.user.id)
      except Exception as e:
         print(e.message)

      print(user)

      user.first_name = first_name
      user.last_name = last_name
      user.username = username
      user.email = email

      if password != None and password != "":
         user.set_password(password)

      user.save()
      messages.success(request,'Profile Updated Successfully !')
      return redirect('profile')