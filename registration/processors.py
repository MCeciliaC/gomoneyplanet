from .models import Profile, Seller, User 
from core.models import Social
from django.contrib.auth import get_user_model

def userlog(request):
    seller= Seller.objects.all()
    client= Profile.objects.all()
    red= Social.objects.all()
    return {'sellerlog': seller, 'clientlog': client, 'socialred': red}

