"""crypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from core.views import HomePageView, QuestionListView, PlanView, SellerView, Error404View, Error505View, ClientUpdate, ClientCreate, ClientDelete
from django.conf.urls import handler404, handler500
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HomePageView.as_view(), name="home"), 
    path('panel/<user_id>/', login_required(views.panel), name="panel"), #<> para campo dinamico
    path('about/', QuestionListView.as_view(), name='about'),
    path('plan/', login_required(PlanView.as_view()), name='plan'),
    path('seller/',login_required( SellerView.as_view()), name='seller'),
    path('create/', login_required(ClientCreate.as_view()), name='create'),
    path('update/<int:pk>/', login_required(ClientUpdate.as_view()), name='update'),
    path('delete/<int:pk>/', login_required(ClientDelete.as_view()), name='delete'),
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

handler404= Error404View.as_view()
handler500= Error505View.as_error_view()