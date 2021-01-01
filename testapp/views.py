from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm,EditUserForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,logout,login,update_session_auth_hash
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created successfully')
    else:
        fm=SignUpForm()
    return render(request,'testapp/register.html',{'user':fm})
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pword=fm.cleaned_data['password']
                user=authenticate(username=uname,password=pword)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            fm=AuthenticationForm()
        return render(request,'testapp/login.html',{'form':fm})
    else:
        return redirect('profile')
def profile_view(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = EditUserForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated')
                fm.save()
        else:
            fm = EditUserForm(instance=request.user)
        return render(request, 'testapp/profile.html',{'name':request.user,'form':fm})
    else:
        return redirect('login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')
def passwrod_change(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST) # using old pass method
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user) #after password change session well be update and visited profile
                #other wise logout u profile if u are not used
                messages.success(request,'Password Change successfully....!')
                return redirect('profile')
        else:
            fm=PasswordChangeForm(user=request.user)
    else:
        return redirect('login_view')
    return render(request,'testapp/password.html',{'form':fm})

#password change without old password
def passwrod_change1(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            fm=SetPasswordForm(user=request.user,data=request.POST) # using old pass method
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user) #after password change session well be update and visited profile
                #other wise logout u profile if u are not used
                messages.success(request,'Password Change successfully....!')
                return redirect('profile')
        else:
            fm=SetPasswordForm(user=request.user)
    else:
        return redirect('login_view')
    return render(request,'testapp/password1.html',{'form':fm})
