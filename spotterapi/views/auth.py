from sqlite3 import Date
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import datetime


from spotterapi.models.Profile import Profile



@api_view(['POST'])
@permission_classes([AllowAny])

# request will be an object with information such as username and password
def login_user(request):
    '''Handles the authentication of a gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):

    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    
# if the program finds an existing user with that username, set data to error message

    check_user = User.objects.filter(username = request.data['username'])
    if len(check_user) > 0:
        data = { 'username error': "username taken"} 
        pass

    else:
    
        new_user = User.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email = request.data['email'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            
        )

        # Now save the extra info in the levelupapi_gamer table
        profile = Profile.objects.create(
            bio=request.data['bio'],
            user=new_user,
            # profile_image_url = request.data['profile_image_url'],
            created_on = datetime.datetime.now(),
            active = True

        )

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=profile.user)
        # Return the token to the client
        


        data = { 'token': token.key }

    return Response(data)