from django.conf import settings
from django.contrib.auth.models import User
from django.forms.widgets import DateTimeInput
from django.http.response import HttpResponse, HttpResponseRedirect
from insta.forms import CommentForm, NewPostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from insta.models import Comment, Image, Profile
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username, email=email,password=password)
            subject = 'Uh-huh, glad you are here!! Welcome to Insta_Clone'
            message = f'Hi {user.username}, thank you for registering with Insta_Clone.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse('Thank you for registering with Insta_Clone')
    else:
        form = SignUpForm()
    return render(request, 'registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()
  
    return render(request,'index.html',{"posts":posts,"profile":profile,"comment":comment})

