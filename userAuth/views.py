from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LoginView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):                                     # Add a POST request
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})        # Work with a serialiser and use the data from outside, data=request.data
        serializer.is_valid(raise_exception=True)                               # If request not valid raise Error
        user = serializer.validated_data['user']                                # Get the user from the POST request
        token, created = Token.objects.get_or_create(user=user)                 # Get or Create Token if user loged in
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        

class LogoutView(APIView):
  permission_classes = (IsAuthenticated,)
  
  def post(self, request):
    request.user.auth_token.delete()
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)