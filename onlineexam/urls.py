from django.contrib import admin
from django.urls import path
from quiz import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome),
    path('quiz/',views.quiz),
    path('result/',views.result),
    path('saveans/',views.saveans),


]
