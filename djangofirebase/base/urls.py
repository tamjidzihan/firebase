from django.urls import path
from . import views



urlpatterns = [
    path('', views.main, name="main"),
    path('index/', views.index, name="index"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="registerPage"),
    # path('forgetpass/', views.forgetpassPage, name="forgetPassPage"),
    path('postsign/', views.postsignin, name="postsignin"),
    path('logout/', views.logout, name="logout"),
    path('createblog/',views.create_blog,name='createblog')

]