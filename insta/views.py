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
