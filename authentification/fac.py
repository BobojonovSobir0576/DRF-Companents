# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class FacebookTokenView(APIView):
    def post(self, request):
        # Retrieve the Facebook authorization code from the request data
        code = request.data.get('code')

        # Exchange the authorization code for an access token
        access_token_url = 'https://graph.facebook.com/v13.0/oauth/access_token'
        params = {
            'client_id': '863244545502688',
            'client_secret': '8d9a789122fc5f51ab48d03831412c45',
            'code': code,
            'redirect_uri': 'http://127.0.0.1:8000/docs',
        }

        response = requests.get(access_token_url, params=params)
        data = response.json()

        # Check if the response contains the access token
        if 'access_token' in data:
            access_token = data['access_token']
            return Response({'access_token': access_token})
        else:
            return Response({'error': 'Unable to obtain access token'}, status=400)
