from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash,get_user_model
from django.contrib import messages
from .forms import SignUpForm,UserProfileForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .models import UserProfile
# Create your views here.

UserModel = get_user_model()


def loginuser(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homeview')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Invalid Username or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def logoutuser(request):
    logout(request)
    messages.success(request, 'Succesfully logged out')
    return redirect('homeview')

def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            messages.success(request,'Successfully created account')
            messages.info(request,'Activate Your Account that provided your email!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# def signupview(request):
#     if request.method=="POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your Account'
#             message = render_to_string('accounts/account.html',{
#                 'user':user,
#                 'domain':current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':default_token_generator.make_token(user),
#             })
#             send_mail = form.cleaned_data.get('email')
#             email = EmailMessage(mail_subject,message,to=[send_mail])
#             email.send()
#             messages.success(request,'Successfully created account')
#             messages.info(request,'Activate Your Account that provided your email!')
#             return redirect('login')
        
#     else:
#         form=SignUpForm
#     return render(request, 'accounts/signup.html',{'form':form})

# def activate(request,uidb64,token):
#     try:
#         uid=urlsafe_base64_decode(uidb64).decode()
#         user=UserModel._default_manager.get(pk=uid)
#     except(TypeError,ValueError,OverflowError,User.DoesNotExist):
#         user=None
#     if user is not None and default_token_generator.check_token(user,token):
#         user.is_active=True
#         user.save()
#         messages.success(request,"Your account is activated now, You may login")
#         return redirect('login')
#     else:
#         messages.warning(request, "activation link is invalid")
#         return redirect('signup')

def change_passwordview(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect('homeview')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_pass.html',{'form':form})

def userProfile(request):
    try:
        instance = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance = None

    if request.method == 'POST':
        if instance:
            form = UserProfileForm(request.POST,request.FILES,instance=instance)
        else:
            form = UserProfileForm(request.POST,request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request,'Successfully saved your profile')
            return redirect('homeview')
    
    else:
        form = UserProfileForm(instance=instance)
        context = {
            'form':form,
        }
    return render(request, 'accounts/userproCreate.html',context)

def ownerprofile(request):
    user=request.user
    return render(request,'accounts/userprofile.html',{'user':user})

def otherprofile(request,username):
    user=User.objects.get(username=username)
    return render(request,'accounts/otherprofile.html',{'user':user})