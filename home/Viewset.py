from rest_framework import viewsets
from django.contrib.auth.models import User
from home.models import Contact
from home.serializer import UserSerializer
from home.serializer import ContactSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer