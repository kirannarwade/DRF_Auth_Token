from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerialzer, UserDataSerialzer
from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class GetData(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = User.objects.all()
        serialzer = UserSerialzer(user_data, many=True)
        print(request.user)
        return Response(serialzer.data)



class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerialzer(data=request.data)

        if not serializer.is_valid():
            return Response({"status":401, "errors":serializer.errors, "message":"something went wrong"})

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        token_obj, _  = Token.objects.get_or_create(user=user)



        return Response({"status":200, "payload":serializer.data, "token":str(token_obj), "message":"your data is saved"})


