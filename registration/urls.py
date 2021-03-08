from django.urls import path
from .views import RegistrationView#, SignUpView
  
from .views import VerificationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    #path('signup/', SignUpView.as_view(), name="signup"),
    path('register/', RegistrationView.as_view(), name="register"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),

]


