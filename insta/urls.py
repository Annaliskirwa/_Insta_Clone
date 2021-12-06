from django.urls import path
# from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='home'),
    path('profile/<username>/', views.profile, name='profile'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('like/<id>', views.like, name='like'),
    path('post/<id>', views.comment, name='comment'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
